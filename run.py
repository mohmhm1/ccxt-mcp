from src.server import mcp
import src.tools
import src.resources
import src.prompts
import logging
import sys
import os

if __name__ == "__main__":
    # Log to both console and file
    logging.basicConfig(level=logging.INFO, handlers=[
        logging.StreamHandler(sys.stdout)
    ])
    logging.info(" Starting FastMCP CCXT server...")

    # Cloud mode: FastMCP expects an HTTP server on port 8080
    mcp.run(host="0.0.0.0", port=8080)
