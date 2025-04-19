from typing import Dict
from mcp.server.fastmcp import FastMCP
import ccxt

# Create a shared MCP instance
mcp = FastMCP("CCXT Trading Server", dependencies=["ccxt"]) 
# Global exchange instances cache
_exchanges: Dict[str, ccxt.Exchange] = {}
