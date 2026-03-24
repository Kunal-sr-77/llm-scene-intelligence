import json
from evaluator.validator import validate_output
from analysis.error_analysis import analyze_errors
from metrics.tracker import MetricsTracker


def evaluate_dataset(file_path="dataset.json"):
    with open(file_path, "r") as f:
        dataset = json.load(f)

    tracker = MetricsTracker()

    for sample in dataset:
        scene = sample["input"]
        output = sample["output"]

        errors = validate_output(scene, output)
        tracker.update(errors)

    print("\nDATASET EVALUATION:\n")
    print(tracker.report())


if __name__ == "__main__":
    evaluate_dataset() 