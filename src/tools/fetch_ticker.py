from typing import Any, Dict
from ..server import mcp
from .exchange import get_exchange

@mcp.tool()
def fetch_ticker(exchange_id: str, symbol: str, testnet: bool = False) -> Dict[str, Any]:
    """Fetch ticker data for a symbol on a specific exchange.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        symbol: The trading pair symbol (e.g., 'BTC/USDT')
        testnet: Whether to use testnet (default: False)
    """
    exchange = get_exchange(exchange_id, testnet)
    return exchange.fetch_ticker(symbol) 
