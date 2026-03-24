from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

from generator.llm_generator import generate_response
from parser.json_parser import parse_llm_output
from evaluator.validator import validate_output
from analysis.error_analysis import analyze_errors
from metrics.tracker import MetricsTracker


app = FastAPI(title="Autonomous Driving Dataset API")


# -------------------------
# Request Schema
# -------------------------
class SceneInput(BaseModel):
    objects: List[str]


# -------------------------
# Root Endpoint
# -------------------------
@app.get("/")
def root():
    return {"message": "API is running"}


# -------------------------
# 1. Analyze Scene
# -------------------------
@app.post("/analyze")
def analyze_scene(data: SceneInput):
    try:
        scene = data.objects

        raw = generate_response(scene)
        parsed = parse_llm_output(raw)

        errors = validate_output(scene, parsed)
        analysis = analyze_errors(errors)

        is_valid = len(errors) == 0

        return {
            "input": scene,
            "output": parsed,
            "is_valid": is_valid,
            "errors": errors,
            "analysis": analysis
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# 2. Compare Prompts
# -------------------------
@app.post("/compare")
def compare_prompts(data: SceneInput):
    try:
        scene = data.objects

        results = {}

        for prompt in ["prompt_v1.txt", "prompt_v2.txt", "prompt_v3.txt"]:
            raw = generate_response(scene, f"prompts/{prompt}")
            parsed = parse_llm_output(raw)

            errors = validate_output(scene, parsed)
            analysis = analyze_errors(errors)

            is_valid = len(errors) == 0

            results[prompt] = {
                "output": parsed,
                "is_valid": is_valid,
                "errors": errors,
                "analysis": analysis
            }

        return {
            "input": scene,
            "comparison": results
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# 3. Dataset Metrics
# -------------------------
@app.get("/metrics")
def get_metrics():
    try:
        with open("dataset.json", "r") as f:
            dataset = json.load(f)

        tracker = MetricsTracker()

        for sample in dataset:
            scene = sample["input"]
            output = sample["output"]

            errors = validate_output(scene, output)
            tracker.update(errors)

        return tracker.report()

    except Exception as e:
        return {"error": str(e)} 