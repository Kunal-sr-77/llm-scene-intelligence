from generator.llm_generator import generate_response
from parser.json_parser import parse_llm_output
from evaluator.validator import validate_output
from analysis.error_analysis import analyze_errors
from metrics.tracker import MetricsTracker

def run_pipeline(prompt_path):
    scenes = [
    ["person", "car"],
    ["car"],
    [],
    ["person"],
    ["car", "car"],
    
    # 🔥 Edge cases
    ["person", "car", "car"],
    ["person", "person"],
    ["car", "bicycle"],
    ["person", "truck"],
    ["dog"],  # unknown object
    ["person", "dog", "car"],
] 

    tracker = MetricsTracker()

    for scene in scenes:
        raw_output = generate_response(scene, prompt_path)
        parsed_output = parse_llm_output(raw_output)

        errors = validate_output(scene, parsed_output)
        tracker.update(errors)

    return tracker.report()


if __name__ == "__main__":
    print("\n--- PROMPT V1 RESULTS ---")
    v1_results = run_pipeline("prompts/prompt_v1.txt")
    print(v1_results)

    print("\n--- PROMPT V2 RESULTS ---")
    v2_results = run_pipeline("prompts/prompt_v2.txt")
    print(v2_results) 
    
    print("\n--- PROMPT V3 RESULTS ---")
v3_results = run_pipeline("prompts/prompt_v3.txt")
print(v3_results)