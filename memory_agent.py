memory = []

def store_memory(text):
    memory.append(text)

def retrieve_memory(query):
    for item in memory:
        if query.lower() in item.lower():
            return item
    return None