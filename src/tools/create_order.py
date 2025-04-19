from typing import Any, Dict, Optional
from ..server import mcp
from .exchange import get_exchange

@mcp.tool()
def create_order(
    exchange_id: str,
    symbol: str,
    type: str,
    side: str,
    amount: float,
    price: Optional[float] = None,
    params: Optional[Dict[str, Any]] = None,
    testnet: bool = False
) -> Dict[str, Any]:
    """Create a new order on the exchange.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        symbol: The trading pair symbol (e.g., 'BTC/USDT')
        type: Order type ('market', 'limit', etc.)
        side: Order side ('buy' or 'sell')
        amount: Order amount
        price: Order price (required for limit orders)
        params: Additional parameters (optional)
        testnet: Whether to use testnet (default: False)
    """
    exchange = get_exchange(exchange_id, testnet)
    return exchange.create_order(symbol, type, side, amount, price, params or {}) 
