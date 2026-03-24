# LLM Scene Intelligence

Evaluation-driven LLM system for generating and validating autonomous driving decisions with measurable performance improvements.
This project focuses on evaluating and improving LLM reliability rather than just generating outputs.

---

## Highlights

* Improved decision accuracy from **45.45% → 81.82%** through prompt optimization
* Evaluated **50+ synthetic driving scenarios** using rule-based validation
* Identified key failure mode: **vague_action (26% of errors)**
* Built end-to-end pipeline with **LLM + validation + error analysis + API deployment**

---

## Problem Statement

Large Language Models can generate reasoning for autonomous driving scenarios, but their outputs are often inconsistent, vague, or unsafe for real-world applications.

Key challenges:

* Lack of structured outputs for downstream systems
* Vague or non-actionable recommendations
* No built-in evaluation mechanism to verify correctness

---

## Solution Overview

This project implements a complete pipeline to:

* Generate structured driving decisions using LLMs
* Enforce JSON outputs for consistency
* Validate outputs using safety-aware rules
* Analyze failure patterns
* Improve performance through prompt engineering

---

## System Architecture

Scene Input (objects)
→ Prompt Engine
→ LLM Generation
→ Structured Output (JSON)
→ Validation Engine
→ Error Analysis
→ Metrics Tracking
→ Improvement Loop

---

## Results

### Prompt Evaluation

* Prompt v1 accuracy: 45.45%
* Prompt v2 accuracy: 81.82%
* Prompt v3 accuracy: 63.64%

### Dataset Evaluation

* Total samples: 50
* Accuracy: 70%

Error distribution:

* vague_action: 13
* risk_mismatch: 2

Key Insight:
Most failures were due to vague action recommendations, highlighting the importance of explicit safety constraints in prompts.

---

## Prompt Engineering

Three prompt strategies were evaluated:

* **Prompt v1**: Basic instructions, resulted in vague and inconsistent outputs
* **Prompt v2**: Added strict safety constraints, significantly improved accuracy
* **Prompt v3**: Over-constrained, reduced reasoning flexibility

Conclusion:
Balancing constraint and flexibility is critical for reliable LLM behavior.

---

## Dataset Generation

Synthetic dataset is generated using LLM.

**Note:** This system uses synthetic scene inputs for controlled evaluation of LLM decision-making behavior.

Input:

* List of detected objects (e.g., ["person", "car"])

Output:

* Scene description
* Risk level
* Recommended action

Stored in:

* dataset.json

---

## API Endpoints

Base URL:
http://127.0.0.1:8000

### POST /analyze

**Request:**

```json
{
  "objects": ["person", "car"]
}
```

**Returns:**

* output (LLM decision)
* is_valid (validation result)
* errors
* analysis

---

### POST /compare

**Request:**

```json
{
  "objects": ["person"]
}
```

**Returns:**

* outputs from prompt_v1, prompt_v2, prompt_v3
* validation results

---

### GET /metrics

**Returns:**

* total_samples
* accuracy
* error_distribution

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kunal-sr-77/llm-scene-intelligence.git
cd llm-scene-intelligence
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create Environment File

```bash
touch .env
```

---

### 5. Add API Key

```bash
echo "OPENROUTER_API_KEY=your_api_key" >> .env
```

---

## Running the System

```bash
uvicorn api:app --reload
```

Access API documentation:
http://127.0.0.1:8000/docs

---

## Testing the System

```bash
# Generate dataset
python -m pipeline.generate_dataset

# Evaluate dataset
python -m pipeline.evaluate_dataset
```

---

## Tech Stack

* Python
* FastAPI
* OpenRouter (LLM)
* Pydantic
* Rule-based validation system

---

## Why This Matters

LLM outputs are increasingly used in safety-critical systems such as autonomous driving.
However, their reliability is often not systematically evaluated.

This project demonstrates how to:

* Generate structured datasets using LLMs
* Evaluate decision quality using rule-based validation
* Identify failure patterns in model outputs
* Improve system performance through prompt engineering

This aligns with real-world ADAS development workflows.

---

## Key Learnings

* Designing evaluation pipelines for LLM outputs
* Importance of structured data in AI systems
* Identifying failure patterns in generative models
* Trade-offs in prompt engineering
* Building reliable AI systems for safety-critical domains

---

## Future Improvements

* Stronger semantic validation for actions
* Integration with real perception systems (YOLO)
* Larger and more diverse dataset generation
* Automated prompt optimization
* Model fine-tuning for domain-specific behavior

---
