from agents.base import create_agent

reviewer_agent = create_agent(
    system_prompt="""
You are an expert resume reviewer.

Return JSON with:
- score (1 to 10)
- strengths (list)
- weaknesses (list)
- suggestions (list)

Be honest and professional.
"""
)
