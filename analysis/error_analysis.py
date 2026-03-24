def analyze_errors(errors):
    analysis_report = []

    for error in errors:
        if error["type"] == "risk_mismatch":
            analysis_report.append({
                "error_type": "risk_mismatch",
                "reason": f"Expected risk '{error['expected']}' but got '{error['actual']}'",
                "suggestion": "Adjust prompt to enforce stricter risk rules for detected objects"
            })

        elif error["type"] == "unsafe_action":
            analysis_report.append({
                "error_type": "unsafe_action",
                "reason": error["reason"],
                "suggestion": "Ensure prompt emphasizes safe braking or stopping for high-risk scenarios"
            })

        else:
            analysis_report.append({
                "error_type": "unknown",
                "reason": "Unrecognized error type",
                "suggestion": "Review evaluation logic"
            })

    return analysis_report