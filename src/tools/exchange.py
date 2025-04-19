import os
from typing import Dict, Optional
import ccxt
from dotenv import load_dotenv
from ..server import mcp
from ..server import _exchanges
import logging
# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

@mcp.tool()
def get_exchange(exchange_id: str, testnet: bool = False) -> ccxt.Exchange:
    """Get or create an exchange instance with optional testnet support.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        testnet: Whether to use testnet (default: False)
    
    Returns:
        An initialized CCXT exchange instance
    """
    cache_key = f"{exchange_id}{'_testnet' if testnet else ''}"
    
    if cache_key in _exchanges:
        return _exchanges[cache_key]
    
    api_key = os.getenv(f"{exchange_id.upper()}_APIKEY")
    secret = os.getenv(f"{exchange_id.upper()}_SECRET")
    # Initialize exchange
    config = {
        'apiKey': api_key,
        'secret': secret,
        'enableRateLimit': True,
    }
    exchange = getattr(ccxt, exchange_id)(config)
    if testnet:
        exchange.set_sandbox_mode(enable=True)

    exchange.load_markets()

    _exchanges[cache_key] = exchange
    
    return _exchanges[cache_key] 
