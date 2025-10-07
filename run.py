from src.server import mcp
import src.tools
import src.resources
import src.prompts

# Expose async entrypoint for FastMCP Cloud
async def main():
    # nothing fancy here — the cloud runtime will await this internally
    return mcp
