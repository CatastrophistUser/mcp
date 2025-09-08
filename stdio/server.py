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

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."



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