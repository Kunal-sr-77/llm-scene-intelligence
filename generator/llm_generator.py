import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize client (OpenRouter compatible)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def load_prompt(prompt_path: str) -> str:
    with open(prompt_path, "r") as file:
        return file.read()


def generate_response(objects, prompt_path="prompts/prompt_v1.txt"):
    # Load prompt template
    prompt_template = load_prompt(prompt_path)

    # Inject objects into prompt
    prompt = prompt_template.replace("{objects}", str(objects))

    # Call LLM
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",  # you can change later
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extract output
    output = response.choices[0].message.content

    return output