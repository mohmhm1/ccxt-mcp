from ..server import mcp

@mcp.prompt()
def order_management(order_type: str, side: str) -> str:
    """Get guidance on managing a specific type of order.
    
    Args:
        order_type: The type of order ('market', 'limit', 'stop', etc.)
        side: The order side ('buy' or 'sell')
    """
    return f"""
Please provide guidance on managing a {order_type} {side} order.
Consider the following aspects:
1. Best practices for order placement
2. Risk management considerations
3. Common pitfalls to avoid
4. Monitoring and adjustment strategies
5. Exit strategies
""" 
