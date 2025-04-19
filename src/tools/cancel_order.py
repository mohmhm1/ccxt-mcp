from typing import Any, Dict, Optional
from .exchange import get_exchange
from ..server import mcp


@mcp.tool()
def cancel_order(
    exchange_id: str,
    order_id: str,
    symbol: Optional[str] = None,
    testnet: bool = False
) -> Dict[str, Any]:
    """Cancel an order on the exchange.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        order_id: The ID of the order to cancel
        symbol: The trading pair symbol (optional, some exchanges require it)
        testnet: Whether to use testnet (default: False)
    """
    exchange = get_exchange(exchange_id, testnet)
    return exchange.cancel_order(order_id, symbol) 
