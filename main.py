import os
from scrapegraphai.graphs import SmartScraperGraph

# 1. Setup Handover Pro with Login Credentials
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

# 2. Define the Intelligence Target
smart_scraper_graph = SmartScraperGraph(
    prompt="Log in and extract the November 2025 Dubai market sales value and volume.",
    source="https://dxbinteract.com/login", 
    config=graph_config
)

# 3. Execute
print("Handover Pro: Commencing fresh authenticated scan...")
result = smart_scraper_graph.run()
print("--- HANDOVER PRO: RESULTS ---")
print(result)
