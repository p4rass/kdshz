# pipeline/task2_store.py

CHUNK_STORE = []


def chunk_text(text, chunk_size=500, overlap=100):
    """
    Splits text into overlapping chunks.
    """
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def store_novel(novel_text):
    """
    Task 2:
    - Chunk the novel
    - Store chunks in a global store
    """

    global CHUNK_STORE
    CHUNK_STORE.clear()

    chunks = chunk_text(novel_text)

    for idx, chunk in enumerate(chunks):
        CHUNK_STORE.append({
            "id": idx,
            "text": chunk
        })

    print(f"[Task 2] Stored {len(CHUNK_STORE)} chunks.")
