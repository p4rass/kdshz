from pipeline.task1_claims import extract_claims
from pipeline.task2_store import store_novel
from pipeline.task3_retrieve import retrieve_passages
from pipeline.task4_verify import verify_claim
from pipeline.task5_aggregate import evaluate_claim
from pipeline.task6_global import global_decision
from pipeline.task7_explain import generate_explanation


def main():
    # =========================
    # Load input data
    # =========================
    with open("data/novel.txt", "r", encoding="utf-8") as f:
        novel_text = f.read()

    with open("data/backstory.txt", "r", encoding="utf-8") as f:
        backstory_text = f.read()

    # =========================
    # Task 1: Extract claims
    # =========================
    claims = extract_claims(backstory_text)

    # =========================
    # Task 2: Store novel
    # =========================
    store_novel(novel_text)

    claim_results = {}

    # =========================
    # Tasks 3–5: Evidence + verification + aggregation
    # =========================
    for claim in claims:
        passages = retrieve_passages(claim)
        verdicts = [verify_claim(claim, p) for p in passages]
        claim_results[claim] = evaluate_claim(verdicts)

    # =========================
    # Task 6: Global decision
    # =========================
    final_label = global_decision(claim_results)

    # =========================
    # Task 7: Explanation
    # =========================
    explanation = generate_explanation(claim_results)

    # =========================
    # Final Output
    # =========================
    print("\n========== RESULTS ==========\n")

    print("Claims and verdicts:")
    for claim, status in claim_results.items():
        print(f"- {claim} → {status}")

    print("\nFinal label:", final_label)
    print("\nExplanation:")
    print(explanation)

    print("\n=============================\n")


if __name__ == "__main__":
    main()
