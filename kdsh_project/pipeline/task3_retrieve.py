# pipeline/task3_retrieve.py

from pipeline.task2_store import CHUNK_STORE


def retrieve_passages(claim, top_k=3):
    """
    Task 3:
    Given a claim, retrieve top-K relevant novel chunks.
    """

    claim_words = set(claim.lower().split())

    scored_chunks = []

    for chunk in CHUNK_STORE:
        chunk_words = set(chunk["text"].lower().split())
        score = len(claim_words.intersection(chunk_words))

        scored_chunks.append((score, chunk["text"]))

    # Sort by score descending
    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    # Take top-K non-zero matches
    top_chunks = [text for score, text in scored_chunks if score > 0][:top_k]

    return top_chunks
