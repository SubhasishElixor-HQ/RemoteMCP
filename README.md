# 🌐 Remote MCP Server

A simple **Remote Model Context Protocol (MCP) Server** built with **Python** and **FastMCP**. This project demonstrates how to create MCP tools and resources and expose them over **HTTP** for remote AI-client access.

## 🧠 Architecture

```text
┌───────────────┐
│   AI Client   │
│ Claude / MCP  │
└───────┬───────┘
        │ HTTP
        ▼
┌───────────────────┐
│  Remote MCP Server│
│      FastMCP      │
└─────────┬─────────┘
          │
      ┌───┴────┐
      ▼        ▼
    Tools   Resources
```

## 🛠️ Tech Stack

* Python 3.11+
* FastMCP
* Model Context Protocol (MCP)
* uv
* HTTP
 README.md
```

## ⚙️ 1. Create Project

Install FastMCP:

```powershell
uv add fastmcp
```

## 🧑‍💻 2. Create `app.py`

```python
from fastmcp import FastMCP
import random

mcp = FastMCP("Simple Calculator Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def random_number(
    min_value: int = 1,
    max_value: int = 100
) -> int:
    """Generate a random number."""
    return random.randint(min_value, max_value)


@mcp.resource("info://server")
def server_info() -> dict:
    """Get server information."""
    return {
        "name": "Simple Calculator Server",
        "tools": ["add", "random_number"]
    }


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )
```

## ▶️ 3. Run the Remote MCP Server

Run directly with Python:

```powershell
uv run python app.py
```

Or using FastMCP:

```powershell
uv run fastmcp run app.py --transport http --host 0.0.0.0 --port 8000
```

Server:

```text
http://localhost:8000
```

## 🔍 4. Test with MCP Inspector

Use the FastMCP Inspector command available in your installed version:

```powershell
uv run fastmcp dev inspector app.py
```

Check available commands if needed:

```powershell
uv run fastmcp --help
```

## 🔄 Request Flow

```text
AI Client
   │
   │ MCP / HTTP
   ▼
FastMCP Server
   │
   ├── add()
   ├── random_number()
   └── info://server
   │
   ▼
Tool / Resource Result
   │
   ▼
AI Client
```

## 🔐 Production

For public deployment, use:

* HTTPS
* Authentication
* Authorization
* Input validation
* Rate limiting
* Logging
* Secret management

Development:

```text
http://localhost:8000
```

Production:

```text
https://your-mcp-server.com
```

## 🚀 Roadmap

* [x] Create MCP server
* [x] Add tools
* [x] Add resources
* [x] HTTP transport
* [ ] MCP Inspector testing
* [ ] Database integration
* [ ] API integration
* [ ] Authentication
* [ ] Docker deployment
* [ ] Cloud deployment

## 👨‍💻 Author

**Subhasish Sahoo**
B.Tech CSE — AI/ML

**Interests:** AI • ML • GenAI • LLM • RAG • AI Agents • MCP • FastAPI
