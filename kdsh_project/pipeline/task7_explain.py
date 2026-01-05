def generate_explanation(claim_results):
    """
    Task 7:
    Generate a human-readable explanation for the final decision.

    Input:
        claim_results: dict {claim: "PASS"/"FAIL"}

    Output:
        explanation string
    """

    failed_claims = [
        claim for claim, status in claim_results.items()
        if status == "FAIL"
    ]

    if not failed_claims:
        return "All backstory claims are consistent with the novel."

    explanation_lines = [
        "The backstory is inconsistent with the novel due to the following claim(s):"
    ]

    for claim in failed_claims:
        explanation_lines.append(f"- {claim}")

    return "\n".join(explanation_lines)
