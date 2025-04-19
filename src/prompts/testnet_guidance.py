from ..server import mcp

@mcp.prompt()
def testnet_guidance(exchange_id: str) -> str:
    """Get guidance on using testnet for a specific exchange.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
    """
    return f"""
Please provide guidance on using the {exchange_id} testnet.
Consider the following aspects:
1. How to set up testnet access
2. Differences between testnet and mainnet
3. Available testnet features
4. Limitations and restrictions
5. Best practices for testing
""" 
