import json
import random
from generator.llm_generator import generate_response
from parser.json_parser import parse_llm_output

# Possible objects
OBJECT_POOL = ["person", "car", "truck", "bicycle", "dog"]

def generate_random_scene():
    num_objects = random.randint(0, 3)
    return random.sample(OBJECT_POOL, num_objects)


def generate_dataset(num_samples=50):
    dataset = []

    for _ in range(num_samples):
        scene = generate_random_scene()

        raw = generate_response(scene)
        parsed = parse_llm_output(raw)

        dataset.append({
            "input": scene,
            "output": parsed
        })

    with open("dataset.json", "w") as f:
        json.dump(dataset, f, indent=2)

    print(f"Generated {num_samples} samples.")


if __name__ == "__main__":
    generate_dataset(50) 