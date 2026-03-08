def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """

    ref_bin_total = sum(reference_counts)
    prod_bin_total = sum(production_counts)
    TVD = 0
    for i in range(len(reference_counts)):
        ref_p = reference_counts[i] / ref_bin_total
        prod_p = production_counts[i] / prod_bin_total

        TVD += abs(ref_p - prod_p)

    TVD /= 2

    ans = {
        "score": TVD,
        "drift_detected": TVD > threshold
    }
    return ans