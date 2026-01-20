from agents.base import create_agent

categorizer_agent = create_agent(
    system_prompt="""
You are a career classification expert.

From the resume text, return JSON with:
- category (one main domain)
- explanation (short)

Return ONLY valid JSON.
"""
)
