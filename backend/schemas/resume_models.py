from pydantic import BaseModel
from typing import List

class ResumeInfo(BaseModel):
    name: str
    skills: List[str]
    education: str
    experience: str

class ResumeReview(BaseModel):
    score: int
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]

class CareerAdvice(BaseModel):
    best_roles: List[str]
    missing_skills: List[str]
    roadmap: List[str]

class InterviewPrep(BaseModel):
    questions: List[str]
    tips: List[str]
