from fastmcp import FastMCP
import random

# Create MCP server instance
mcp = FastMCP("Simple Calculator Server")


# Tool 1: Add Two Numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.
    """
    return a + b


# Tool 2: Generate Random Number
@mcp.tool()
def random_number(
    min_value: int = 1,
    max_value: int = 100
) -> int:
    """Generate a random number within a specified range.

    Args:
        min_value: The minimum value of the range.
        max_value: The maximum value of the range.

    Returns:
        A random number within the specified range.
    """
    return random.randint(min_value, max_value)


# Resource: Server Information
@mcp.resource("info://server")
def server_info() -> dict:
    """Get information about the MCP server."""

    return {
        "name": "Simple Calculator Server",
        "description": "An MCP server providing calculator and random number tools.",
        "tools": [
            "add",
            "random_number"
        ],
        "resource": "info://server"
    }


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )