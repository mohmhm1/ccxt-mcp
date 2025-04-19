from typing import Dict, List
from ..server import mcp
from .exchange import get_exchange

@mcp.tool()
def fetch_markets(exchange_id: str, testnet: bool = False, page: int = 1, per_page: int = 25) -> Dict:
    """Fetch markets for a given exchange with pagination.
    
    Args:
        exchange_id: The exchange ID (e.g., 'binance', 'coinbase')
        testnet: Whether to use testnet (default: False)
        page: Page number (default: 1)
        per_page: Number of markets per page (default: 25)
    
    Returns:
        A dictionary containing:
        - markets: List of market dictionaries containing trading pair information
        - total: Total number of markets
        - page: Current page
        - per_page: Number of markets per page
    """
    print(f"Fetching markets for {exchange_id}")
    exchange = get_exchange(exchange_id, testnet)
    markets = exchange.fetch_markets()
    
    # Calculate pagination
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_markets = markets[start_idx:end_idx]
    
    # Simplify to reduce size
    simplified_markets = [{
        'id': market['id'],
        'symbol': market['symbol'],
        'base': market['base'],
        'quote': market['quote'],
        'type': market['type'],
        'active': market['active'],
        'precision': market['precision'],
        'limits': market['limits']
    } for market in paginated_markets]
    
    return {
        'markets': simplified_markets,
        'total': len(markets),
        'page': page,
        'per_page': per_page
    } 
