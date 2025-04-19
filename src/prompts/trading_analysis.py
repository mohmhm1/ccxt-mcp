from ..server import mcp

@mcp.prompt()
def trading_analysis(symbol: str, timeframe: str = '1h') -> str:
    """Analyze trading opportunities for a given symbol.
    
    Args:
        symbol: The trading pair symbol (e.g., 'BTC/USDT')
        timeframe: The timeframe for analysis (e.g., '1h', '4h', '1d')
    """
    return f"""
Please analyze the trading opportunities for {symbol} on the {timeframe} timeframe.
Consider the following aspects:
1. Current market conditions
2. Support and resistance levels
3. Volume analysis
4. Potential entry and exit points
5. Risk management suggestions
""" 
