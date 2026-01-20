from agents.base import create_agent

career_advisor_agent = create_agent(
    system_prompt="""
You are a senior career advisor.

Return JSON with:
- best_roles (list)
- missing_skills (list)
- roadmap (list)
"""
)
