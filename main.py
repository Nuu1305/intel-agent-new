import langchain_compat # This MUST be the first line
import os
from scrapegraphai.graphs import SmartScraperGraph

graph_config = {
    "llm": {
        "api_key": os.getenv("GEMINI_API_KEY"),
        "model": "google_genai/gemini-flash-latest", 
        "api_version": "v1",
    },
    "loader_kwargs": {
        "auth": {
            "username": os.getenv("DXB_EMAIL"),
            "password": os.getenv("DXB_PASSWORD")
        }
    },
    "headless": True 
}

smart_scraper_graph = SmartScraperGraph(
    prompt="Log in and extract the November 2025 Dubai market sales value and volume.",
    source="https://dxbinteract.com/login", 
    config=graph_config
)

print("Handover Pro: Commencing scan with compatibility fix...")
result = smart_scraper_graph.run()
print(result)
