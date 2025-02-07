from fastapi import APIRouter, HTTPException
from services.resume_service import ResumeService

router = APIRouter()

@router.get("/", response_model=dict)
def welcome():
  return {
    "welcome": "Welcome to my resume API. This API is for fetching my resume data.",
    "valid routes": {
      "/full": "Get my full resume",
      "/contact": "Get my contact information",
      "/projects": "Get my projects",
      "/skills": "Get my skills information",
      "/experience": "Get my professional experience",
      "/education": "Get education information"
    }
  }

@router.get("/full", response_model=dict)
async def get_resume():
  try:
    resume = await ResumeService.get_resume()
    return {"resume": resume}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")
  
@router.get("/contact", response_model=dict)
async def get_contact():
  try:
    contact = await ResumeService.get_contact()
    return {"contact": contact}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")

@router.get("/projects", response_model=dict)
async def get_projects():
  try:
    projects = await ResumeService.get_projects()
    return {"projects": projects}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")

@router.get("/skills", response_model=dict)
async def get_skills():
  try:
    skills = await ResumeService.get_skills()
    return {"skills": skills}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")
  
@router.get("/experience", response_model=dict)
async def get_professional_experience():
  try:
    experience = await ResumeService.get_professional_experience()
    return {"experience": experience}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")
  
@router.get("/education", response_model=dict)
async def get_education():
  try:
    education = await ResumeService.get_education()
    return {"education": education}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")