# Subscriptions

It is possible to create subscriptions for certain data to get updates pushed as they happen. These subscriptions are 
blocking until the subscription is closed.

## Storage subscriptions

When a callable is passed as kwarg `subscription_handler` in the `query()` function, there will be a subscription 
created for given storage query. Updates will be pushed to the callable and will block execution until a final value 
is returned. This value will be returned as a result of the query and finally automatically unsubscribed from further 
updates.

```python
def subscription_handler(account_info_obj, update_nr, subscription_id):

    if update_nr == 0:
        print('Initial account data:', account_info_obj.value)

    if update_nr > 0:
        # Do something with the update
        print('Account data changed:', account_info_obj.value)

    # The execution will block until an arbitrary value is returned, which will be the result of the `query`
    if update_nr > 5:
        return account_info_obj


result = substrate.query("System", "Account", ["5GNJqTPyNqANBkUVMN1LPPrxXnFouWXoe2wNSmmEoLctxiZY"],
                         subscription_handler=subscription_handler)

print(result)
```

## Subscribe to multiple storage keys 

To subscribe to multiple storage keys at once, the function `subscribe_storage()` provides the most efficient method.
This will track changes for multiple state entries (storage keys) in just one RPC call to the Substrate node.

Same as for `query()`, updates will be pushed to the `subscription_handler` callable and will block execution until 
a final value is returned. This value will be returned as a result of subscription and finally automatically
unsubscribed from further updates.

```python
def subscription_handler(storage_key, updated_obj, update_nr, subscription_id):
    print(f"Update for {storage_key.params[0]}: {updated_obj.value}")

# Accounts to track
storage_keys = [
    substrate.create_storage_key(
        "System", "Account", ["5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY"]
    ),
    substrate.create_storage_key(
        "System", "Account", ["5FHneW46xGXgs5mUiveU4sbTyGBzmstUspZC92UhjJM694ty"]
    )
]

result = substrate.subscribe_storage(
    storage_keys=storage_keys, subscription_handler=subscription_handler
)
```

## Subscribe to new block headers

```python
def subscription_handler(obj, update_nr, subscription_id):
    print(f"New block #{obj['header']['number']}")

    block = substrate.get_block(block_number=obj['header']['number'])

    for idx, extrinsic in enumerate(block['extrinsics']):
        print(f'# {idx}:  {extrinsic.value}')

    if update_nr > 10:
        return {'message': 'Subscription will cancel when a value is returned', 'updates_processed': update_nr}


result = substrate.subscribe_block_headers(subscription_handler)
```
