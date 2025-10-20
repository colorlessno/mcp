# server.py
from mcp.server.fastmcp import FastMCP
from datetime import datetime
import uuid
from zoneinfo import ZoneInfo

mcp = FastMCP("MCP Server")

@mcp.tool()
def ping(text: str) -> str:
    """Echo back the given text with its length."""
    return f"{text} | len={len(text)}"

@mcp.tool()
def now(tz: str = "local") -> str:
    """Return current time in ISO8601. tz example: 'Asia/Tokyo'."""
    if tz and tz.lower() != "local":
        try:
            return datetime.now(ZoneInfo(tz)).isoformat()
        except Exception:
            # フォールバック（不正なTZ指定時）
            return datetime.now().astimezone().isoformat()
    return datetime.now().astimezone().isoformat()

@mcp.tool()
def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b

@mcp.tool()
def gen_uuid() -> str:
    """Return a random UUID string."""
    return str(uuid.uuid4())

if __name__ == "__main__":
    # stdio で実行（Claude Desktop から子プロセスとして起動される）
    mcp.run()

@mcp.tool()
def health() -> dict:
    """Return runtime info useful for debugging."""
    import sys, platform
    return {
        "python_executable": sys.executable,
        "python_version": platform.python_version(),
        "platform": platform.platform()
    }