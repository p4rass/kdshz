''' pipeline/task4_verify.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client (reads OPENAI_API_KEY automatically)
client = OpenAI()


def verify_claim(claim, passage):
    """
    LLM-based verifier (USE THIS WHEN YOU HAVE OPENAI CREDITS)

    Input:
        claim (str)
        passage (str)

    Output:
        One of: SUPPORT, CONTRADICT, NEUTRAL
    """

    prompt = f"""
You are given a CLAIM and a PASSAGE from a novel.

Decide the relationship between the passage and the claim.

Definitions:
- SUPPORT: The passage clearly supports or confirms the claim.
- CONTRADICT: The passage clearly contradicts or makes the claim impossible.
- NEUTRAL: The passage does not provide relevant information.

Rules:
- Do NOT infer beyond the passage.
- Absence of information is NOT a contradiction.
- If the passage is ambiguous or only loosely related, choose NEUTRAL.

Respond with exactly ONE word:
SUPPORT, CONTRADICT, or NEUTRAL.

CLAIM:
{claim}

PASSAGE:
{passage}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You judge factual consistency between text snippets."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=5,
    )

    verdict = response.choices[0].message.content.strip().upper()

    if verdict not in {"SUPPORT", "CONTRADICT", "NEUTRAL"}:
        return "NEUTRAL"

    return verdict

'''

# ==============================
# TASK 4 — FALLBACK VERIFIER
# ==============================

import subprocess

print("[LLM VERIFY CALLED]")


def verify_claim(claim, passage):
    prompt = f"""
Decide the relationship between the CLAIM and PASSAGE.
Respond with exactly one word: SUPPORT, CONTRADICT, or NEUTRAL.

CLAIM:
{claim}

PASSAGE:
{passage}
"""

    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore",   # 👈 THIS LINE
        timeout=60
    )


    output = result.stdout.strip().upper()

    if "CONTRADICT" in output:
        return "CONTRADICT"
    if "SUPPORT" in output:
        return "SUPPORT"
    return "NEUTRAL"

'''
def verify_claim(claim, passage):
    """
    Improved fallback verifier (NO API).
    Detects obvious contradictions using simple heuristics.
    """

    claim_lower = claim.lower()
    passage_lower = passage.lower()

    # Strong support
    if claim_lower in passage_lower:
        return "SUPPORT"

    # --- Simple contradiction heuristics ---

    # Birthplace contradiction
    if "born in germany" in claim_lower and "born in italy" in passage_lower:
        return "CONTRADICT"

    if "born in italy" in claim_lower and "born in germany" in passage_lower:
        return "CONTRADICT"

    # Violence contradiction
    if "avoid violence" in claim_lower and "violent" in passage_lower:
        return "CONTRADICT"

    if "dislikes aggressive" in claim_lower and "aggressive" in passage_lower:
        return "CONTRADICT"

    return "NEUTRAL"

'''
