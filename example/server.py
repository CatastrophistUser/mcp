from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

# Simple MCP Server
'''Specify the host and port to run the server on for SSE'''
mcp = FastMCP(
    name="MyMCPServer",
    host="0.0.0.0",
    port=8050,
) 

@mcp.tool()
def add(x: int, y: int) -> int:
    return x + y

if __name__ == "__main__":
    transport = "sse"

    if transport == "stdio":
        print("Starting MCP server with stdio transport...")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Starting MCP server with SSE transport...")
        mcp.run(transport="sse")
    else:
        raise ValueError("Invalid transport method")