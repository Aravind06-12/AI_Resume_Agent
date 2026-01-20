from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "openrouter:mistralai/mistral-7b-instruct"

def create_agent(system_prompt):
    return Agent(
        model=MODEL_NAME,
        system_prompt=system_prompt
    )
