from fastapi import APIRouter, HTTPException, Path, Query
from models import StudentRegistration, UpdateEmail
from typing import Dict

router = APIRouter()

# Mock database (In-memory)
students_db: Dict[int, dict] = {}

# 1️⃣ GET Student Information
@router.get("/students/{student_id}")
async def get_student_info(
    student_id: int = Path(..., gt=1000, lt=9999, description="Student ID must be between 1001-9998"),
    include_grades: bool = Query(False, description="Include grades in response"),
    semester: str = Query(None, regex="^(Fall|Spring|Summer)\d{4}$", description="Format: Fall2024, Spring2025, etc.")
):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student = students_db[student_id]
    if include_grades:
        student["grades"] = {"Math": "A", "Science": "B"}  # Mock grades
    return student

# 2️⃣ POST Register Student
@router.post("/students/register")
async def register_student(student: StudentRegistration):
    student_id = len(students_db) + 1001  # Generate unique ID
    students_db[student_id] = student.dict()
    return {"message": "Student registered successfully", "student_id": student_id}

# 3️⃣ PUT Update Student Email
@router.put("/students/{student_id}/email")
async def update_student_email(
    student_id: int = Path(..., gt=1000, lt=9999, description="Student ID must be between 1001-9998"),
    email_data: UpdateEmail = None
):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    students_db[student_id]["email"] = email_data.email
    return {"message": "Email updated successfully"}
