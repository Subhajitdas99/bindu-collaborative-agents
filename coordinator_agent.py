from research_agent import research
from utils.semantic_memory import store_memory, retrieve_memory

def coordinator(query: str):

    # 1️⃣ Try retrieving from memory
    memories = retrieve_memory(query)

    if memories:
          print("🧠 Retrieved knowledge from memory.")
          return f"(From Memory) {memories[0]['text']}"
    # 2️⃣ Otherwise research
    research_result = research(query)

    # 3️⃣ Store the new knowledge
    store_memory(research_result)

    return research_result