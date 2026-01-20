from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber

from agents.resume_parser import resume_parser_agent
from agents.categorizer import categorizer_agent
from agents.reviewer import reviewer_agent
from agents.career_advisor import career_advisor_agent
from agents.interview_coach import interview_coach_agent

app = FastAPI(title="AI Resume Screening & Career Advisor Agent")

# 🔴 VERY IMPORTANT — Enable CORS (frontend → backend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Resume Agent backend running 🚀. Go to /docs to test."}

@app.post("/analyze_resume/")
async def analyze_resume(file: UploadFile = File(...)):

    # 1. Read resume text from PDF
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

    # 2. Resume Parser Agent
    parsed = await resume_parser_agent.run(text)

    # 3. Categorization Agent
    category = await categorizer_agent.run(text)

    # 4. Resume Reviewer Agent
    review = await reviewer_agent.run(text)

    # 5. Career Advisor Agent
    advice = await career_advisor_agent.run(text)

    # 6. Interview Coach Agent
    interview = await interview_coach_agent.run(text)

    # 🔴 IMPORTANT: use .output instead of .data
    return {
        "parsed_info": parsed.output,
        "category": category.output,
        "review": review.output,
        "career_advice": advice.output,
        "interview_prep": interview.output
    }
