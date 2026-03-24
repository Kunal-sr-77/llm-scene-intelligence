
def expected_risk(objects):
    if "person" in objects:
        return "high"
    elif any(obj in objects for obj in ["car", "truck", "bicycle"]):
        return "medium"
    else:
        return "low" 