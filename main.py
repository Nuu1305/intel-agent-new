import asyncio
import os
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

async def run_intelligence_scan():
    # 1. Configure the browser for Stealth and Login
    browser_config = BrowserConfig(
        headless=True,
        verbose=True
    )
    
    # 2. Setup the scan target
    # We use LLM extraction directly with your Gemini Key
    run_config = CrawlerRunConfig(
        word_count_threshold=10,
        extraction_strategy=None, # We'll get raw markdown first for reliability
        cache_mode="bypass"
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        print("Navigating to DXB Interact...")
        # Step A: Attempt to Login using the page interaction feature
        result = await crawler.arun(
            url="https://dxbinteract.com/login",
            config=run_config,
            # This tells the crawler exactly how to log in
            js_code=[
                f"document.querySelector('input[type=\"email\"]').value = '{os.getenv('DXB_EMAIL')}';",
                f"document.querySelector('input[type=\"password\"]').value = '{os.getenv('DXB_PASSWORD')}';",
                "document.querySelector('button[type=\"submit\"]').click();"
            ]
        )
        
        if result.success:
            print("--- HANDOVER PRO: DATA GATHERED ---")
            # We print the first 1000 characters of the dashboard
            print(result.markdown[:1000])
        else:
            print(f"Scan failed: {result.error_message}")

if __name__ == "__main__":
    asyncio.run(run_intelligence_scan())
