from src.server import mcp
import src.tools
import src.resources
import src.prompts
import logging
import sys

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, handlers=[
        logging.FileHandler("logs/mcp_client.log"),
        logging.StreamHandler()
    ])
    logger = logging.getLogger(__name__)
    mcp.run(transport='stdio') 
