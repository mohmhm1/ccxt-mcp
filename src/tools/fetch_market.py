from typing import Dict, Optional
from ..server import mcp
from .exchange import get_exchange

@mcp.tool()
def fetch_market(exchange_id: str, symbol: str, testnet: bool = False) -> Optional[Dict]:
    """Fetch a single market for a given exchange and symbol.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        symbol: The trading pair symbol (e.g., 'BTC/USDT')
        testnet: Whether to use testnet (default: False)
    
    Returns:
        A market dictionary containing trading pair information, or None if not found
    """
    print(f"Fetching market {symbol} for {exchange_id}")
    exchange = get_exchange(exchange_id, testnet)
    markets = exchange.fetch_markets()
    
    # Find the market with matching symbol
    market = next((m for m in markets if m['symbol'] == symbol), None)
    return market
