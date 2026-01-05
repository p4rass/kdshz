def evaluate_claim(verdicts):
    """
    Task 5:
    Aggregate passage-level verdicts for ONE claim.

    Input:
        verdicts: list of strings
                  each in {"SUPPORT", "CONTRADICT", "NEUTRAL"}

    Output:
        "PASS" or "FAIL"
    """

    # Simple, conservative baseline logic
    if "CONTRADICT" in verdicts:
        return "FAIL"

    return "PASS"
