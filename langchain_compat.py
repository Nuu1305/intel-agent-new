import sys
import langchain_core

# This trick redirects old imports to the new locations
# so ScrapeGraphAI stops crashing
if 'langchain.prompts' not in sys.modules:
    import langchain_core.prompts
    sys.modules['langchain.prompts'] = langchain_core.prompts
