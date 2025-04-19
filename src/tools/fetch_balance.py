import logging
from typing import Any, Dict
from ..server import mcp
from .exchange import get_exchange
import os

# Configure logger
logger = logging.getLogger(__name__)

@mcp.tool()
def fetch_balance(
    exchange_id: str,
    testnet: bool = False
) -> Dict[str, Any]:
    """Fetch account balance from the exchange.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        testnet: Whether to use testnet (default: False)
    """
    logger.info(f"Fetching balance for exchange: {exchange_id} (testnet: {testnet})")
    try:
        exchange = get_exchange(exchange_id, testnet)
        balance = exchange.fetch_balance()
        logger.info(f"Successfully fetched balance from {exchange_id}")
        return balance
    except Exception as e:
        logger.error(f"Error fetching balance from {exchange_id}: {str(e)}")
        raise 
