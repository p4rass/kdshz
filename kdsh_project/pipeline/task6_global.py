def global_decision(claim_results):
    """
    Task 6:
    Aggregate all claims into a final decision.

    Input:
        claim_results: dict {claim: "PASS"/"FAIL"}

    Output:
        1 (consistent) or 0 (inconsistent)
    """

    for status in claim_results.values():
        if status == "FAIL":
            return 0

    return 1
