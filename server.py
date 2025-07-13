# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def special_add(a: int, b: int) -> int:
    """Add two numbers with a special rule"""
    return a + b + 1

@mcp.tool
def special_sub(a: int, b: int) -> int:
    """Subtract two numbers with a special rule"""
    return a - b - 1

@mcp.tool
def special_mul(a: int, b: int) -> int:
    """Multiply two numbers with a special rule"""
    return a * b * 1


if __name__ == "__main__":
    mcp.run(
        transport = "http",
        host = "0.0.0.0",
        port = 8000,
        path = "/mcp",
    )
