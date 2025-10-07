from src.server import mcp  # imports app automatically
import src.tools
import src.resources
import src.prompts
import logging
import sys
import os

# For FastMCP Cloud: the platform will use this
app = mcp.app

# For local debugging
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, handlers=[
        logging.StreamHandler(sys.stdout)
    ])
    logging.getLogger(__name__).info("Running MCP locally with STDIO transport...")
    mcp.run(transport="stdio")
