# mcp
Model Context Protocol w/ Python 3.10

Resources
- [Anthropic Blog](https://docs.anthropic.com/en/docs/mcp)
- [MCP Docs](https://modelcontextprotocol.io/docs/getting-started/intro)
- [AI Cookbook](https://github.com/daveebbelaar/ai-cookbook/tree/main/mcp/crash-course)

## About MCP
#### A "USB-C Port" of all AI apps

Model Context Protocol
A standard way to connect tools annd contexts to AI apps/agents

MCP Client
- built into AI apps and sends requests to MCP servers
- discovers server capabilities
- receive data from servers
- manage LLM tool execution

MCP Server
- listens for requests and responds acordingly
- include prompt templates
- resources (data, filesystem, DB; similar to GET request)
- tools (functions, AP, image processing)

## Transport
MCP data can be transported between client and server in 2 ways:

Stdio (local) or HTTP via Server Sent Events (SSE, remote)

![architecture.webp](architecture.webp)