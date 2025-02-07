from data.db import resume_db

class ResumeService:

    @staticmethod
    async def get_resume() -> dict:
        resume = await resume_db.resume.find_one({})
        if resume:
            resume["_id"] = str(resume["_id"])
        return resume or {}
    
    @staticmethod
    async def get_contact() -> dict:
        resume = await resume_db.resume.find_one({})
        if resume:
            resume["_id"] = str(resume["_id"])
        return resume.get("contact", {})
    
    @staticmethod
    async def get_projects() -> dict:
        resume = await resume_db.resume.find_one({})
        if resume:
            resume["_id"] = str(resume["_id"])
        return resume.get("projects", {})

    @staticmethod
    async def get_skills() -> dict:
        resume = await resume_db.resume.find_one({})
        if resume:
            resume["_id"] = str(resume["_id"])
        return resume.get("skills", {})

    @staticmethod
    async def get_professional_experience() -> dict:
        resume = await resume_db.resume.find_one({})
        if resume:
            resume["_id"] = str(resume["_id"])
        return resume.get("professional_experience", {})

    @staticmethod
    async def get_education() -> dict:
        resume = await resume_db.resume.find_one({})
        if resume:
            resume["_id"] = str(resume["_id"])
        return resume.get("education", {})