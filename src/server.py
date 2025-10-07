from mcp.server.fastmcp import FastMCP
import ccxt
from typing import Dict

# Initialize the MCP server (this is just a definition, not a runner)
mcp = FastMCP("CCXT Trading Server", dependencies=["ccxt"])

# Optional: cache of exchanges
_exchanges: Dict[str, ccxt.Exchange] = {}
