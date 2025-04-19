from typing import Any, Dict, Optional
from ..server import mcp
from .exchange import get_exchange

@mcp.tool()
def fetch_order_book(
    exchange_id: str,
    symbol: str,
    limit: Optional[int] = None,
    testnet: bool = False
) -> Dict[str, Any]:
    """Fetch order book data for a symbol on a specific exchange.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        symbol: The trading pair symbol (e.g., 'BTC/USDT')
        limit: Maximum number of orders to fetch (optional)
        testnet: Whether to use testnet (default: False)
    """
    exchange = get_exchange(exchange_id, testnet)
    return exchange.fetch_order_book(symbol, limit) 
