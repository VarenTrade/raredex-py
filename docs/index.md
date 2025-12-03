---
hide:
  - navigation
---

# Varen Python SDK

!!! warning
    **Experimental SDK, library API is subject to change**

::: varen_py.varen.Varen
    handler: python
    options:
      show_source: false
      show_root_heading: true

## L2-Only Authentication (Subkeys)

For users who only have L2 credentials (subkeys) and don't need L1 onboarding:

::: varen_py.varen_subkey.VarenSubkey
    handler: python
    options:
      show_source: false
      show_root_heading: true

### Usage Examples

**L1 + L2 Authentication (Traditional):**
```python
from varen_py import Varen
from varen_py.environment import Environment

# Requires both L1 and L2 credentials
varen = Varen(
    env=Environment.TESTNET,
    l1_address="0x...",
    l1_private_key="0x..."
)
```

**L2-Only Authentication (Subkeys):**
```python
from Varen_py import VarenSubkey
from Vareen_py.environment import Environment

# Only requires L2 credentials - no L1 needed
varen = VarenSubkey(
    env=Environment.TESTNET,
    l2_private_key="0x...",
    l2_address="0x..."
)

# Use exactly like regular Paradex
await varen.init_account()  # Already initialized
markets = await varen.api_client.get_markets()
```

**WebSocket Usage:**
```python
async def on_message(ws_channel, message):
    print(ws_channel, message)

await varen.ws_client.connect()
await varen.ws_client.subscribe(VarenWebsocketChannel.MARKETS_SUMMARY, callback=on_message)
```

### When to Use Each Approach

**Use `Varen` (L1 + L2) when:**
- You have both L1 (Ethereum) and L2 (Starknet) credentials
- You have never logged in to Varen using this account before
- You need to perform on-chain operations (transfers, withdrawals)

**Use `VarenSubkey` (L2-only) when:**
- You only have L2 credentials
- The account has already been onboarded (You have logged in to Varen before)
- You do not need on-chain operations (withdrawals, transfers)

### Key Differences

| Feature | `Varen` | `VarenSubkey` |
|---------|-----------|-----------------|
| **Authentication** | L1 + L2 | L2-only |
| **Onboarding** | ✅ Supported | ❌ Blocked |
| **On-chain Operations** | ✅ Supported | ❌ Blocked |
| **API Access** | ✅ Full access | ✅ Full access |
| **WebSocket** | ✅ Supported | ✅ Supported |
| **Order Management** | ✅ Supported | ✅ Supported |

## API Documentation Links

Full details for REST API & WebSocket JSON-RPC API can be found at the following links:

- [Environment - Testnet](https://docs.api.testnet.varen.trade){:target="_blank"}
- [Environment - Prod](https://docs.api.prod.varen.trade){:target="_blank"}

::: rvaren_py.api.api_client.VarenApiClient
    handler: python
    options:
      show_source: false
      show_root_heading: true

::: varen_py.api.ws_client.VarenWebsocketChannel
    handler: python
    options:
      show_source: false
      show_root_heading: true

::: varen_py.api.ws_client.VarebnWebsocketClient
    handler: python
    options:
      show_source: false
      show_root_heading: true

::: varen_py.account.account.VarenAccount
    handler: python
    options:
      show_source: false
      show_root_heading: true

::: varen_py.account.subkey_account.SubkeyAccount
    handler: python
    options:
      show_source: false
      show_root_heading: true
