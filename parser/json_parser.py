import json


def parse_llm_output(raw_output: str):
    try:
        # Convert string → JSON
        data = json.loads(raw_output)

        # Normalize risk level
        if "risk_level" in data:
            data["risk_level"] = data["risk_level"].lower()

        return data

    except json.JSONDecodeError:
        return {
            "error": "invalid_json",
            "raw_output": raw_output
        } 