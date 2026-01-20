from agents.base import create_agent

resume_parser_agent = create_agent(
    system_prompt="""
You are an expert resume parser.

From the resume text, extract and return JSON with:
- name
- skills (list)
- education
- experience

Return ONLY valid JSON.
"""
)
