from pydantic import BaseModel, EmailStr, Field
from typing import List

class StudentRegistration(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, pattern="^[A-Za-z ]+$", description="Only alphabets and spaces are allowed")
    email: EmailStr
    age: int = Field(..., ge=18, le=30, description="Age must be between 18 and 30")
    courses: List[str] = Field(..., min_items=1, max_items=5, description="Must have between 1 and 5 courses")

    @classmethod
    def validate_courses(cls, courses: List[str]) -> List[str]:
        """Validates course names (length and duplicates)"""
        if len(set(courses)) != len(courses):
            raise ValueError("Duplicate course names are not allowed")
        for course in courses:
            if not (5 <= len(course) <= 30):
                raise ValueError("Each course name must be between 5 and 30 characters")
        return courses

    def __init__(self, **data):
        super().__init__(**data)
        self.courses = self.validate_courses(self.courses)

class UpdateEmail(BaseModel):
    email: EmailStr
