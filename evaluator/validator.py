from evaluator.rules import expected_risk


SAFE_KEYWORDS = ["slow", "stop", "brake"]
VAGUE_WORDS = ["careful", "cautious", "aware", "attention"]


def validate_output(objects, llm_output):
    errors = []

    # -------------------------
    # 1. Risk Validation
    # -------------------------
    expected = expected_risk(objects)
    actual = llm_output.get("risk_level")

    if actual != expected:
        errors.append({
            "type": "risk_mismatch",
            "expected": expected,
            "actual": actual
        })

    # -------------------------
    # 2. Action Validation
    # -------------------------
    action = llm_output.get("recommended_action", "").lower()

    # 2.1 High-risk must include explicit safety action
    if actual == "high":
        if not any(keyword in action for keyword in SAFE_KEYWORDS):
            errors.append({
                "type": "unsafe_action",
                "reason": "High risk but no explicit slow/stop/brake action"
            })

    # 2.2 Detect vague instructions (not acceptable in ADAS)
    if any(word in action for word in VAGUE_WORDS):
        errors.append({
            "type": "vague_action",
            "reason": "Action is vague and not suitable for safety-critical system"
        })

    # -------------------------
    # 3. Basic Consistency Check
    # -------------------------
    description = llm_output.get("scene_description", "").lower()

    for obj in objects:
        if obj not in description:
            errors.append({
                "type": "description_mismatch",
                "reason": f"Object '{obj}' not mentioned in scene description"
            })

    return errors