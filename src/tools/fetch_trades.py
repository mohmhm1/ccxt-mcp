from typing import Any, Dict, Optional
from ..server import mcp
from .exchange import get_exchange

@mcp.tool()
def fetch_trades(
    exchange_id: str,
    symbol: str,
    since: Optional[int] = None,
    limit: Optional[int] = None,
    testnet: bool = False
) -> list[Dict[str, Any]]:
    """Fetch recent trades for a symbol on a specific exchange.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        symbol: The trading pair symbol (e.g., 'BTC/USDT')
        since: Timestamp in milliseconds to fetch trades since (optional)
        limit: Maximum number of trades to fetch (optional)
        testnet: Whether to use testnet (default: False)
    """
    exchange = get_exchange(exchange_id, testnet)
    return exchange.fetch_trades(symbol, since, limit) 
