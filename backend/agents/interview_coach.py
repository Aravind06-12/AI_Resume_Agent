from agents.base import create_agent

interview_coach_agent = create_agent(
    system_prompt="""
You are a technical interview coach.

Return JSON with:
- questions (list of 5)
- tips (list)
"""
)
