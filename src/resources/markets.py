from typing import Dict, List
import ccxt
from ..server import mcp
from ..tools.exchange import get_exchange

@mcp.resource("ccxt://{exchange_id}/markets")
def fetch_markets(exchange_id: str) -> List[Dict]:
    """Fetch all markets for a given exchange.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        testnet: Whether to use testnet (default: False)
    
    Returns:
        A list of market dictionaries containing trading pair information
    """
    exchange = get_exchange(exchange_id)
    markets = exchange.fetch_markets()
    return markets
