'''
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_claims(backstory_text, max_claims=8):
    """
    Input: raw backstory text
    Output: list of atomic claims (strings)
    """

    prompt = f"""
You are given a character backstory.

Your task is to extract at most {max_claims} ATOMIC, FACTUAL OR BEHAVIORAL CLAIMS
that can be verified against a story.

Rules:
- Each claim must be a single clear assertion.
- Do NOT include vague or emotional language.
- Do NOT speculate.
- Claims must be verifiable from text.

Return the output as a numbered list.

Backstory:
\"\"\"
{backstory_text}
\"\"\"
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You extract verifiable claims from text."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    raw_output = response["choices"][0]["message"]["content"]

    claims = []
    for line in raw_output.split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            claim = line.split(".", 1)[1].strip()
            claims.append(claim)

    return claims
'''

# ==============================
# TASK 1 — FALLBACK CLAIM EXTRACTOR
# ==============================

def extract_claims(backstory_text):
    """
    Fallback claim extractor (NO API, NO COST)

    Strategy:
    - Split into sentences
    - Keep factual-looking sentences as claims
    """

    sentences = backstory_text.split(".")
    claims = []

    for s in sentences:
        s = s.strip()
        if not s:
            continue

        # Simple heuristic: keep declarative sentences
        if len(s.split()) >= 3:
            claims.append(s)

    return claims
