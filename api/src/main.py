from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Query
from typing import List
from .db import get_db
from .models import Student
from .schemas import StudentCreate, StudentResponse, StudentUpdate

app = FastAPI()

# @app.lifespan()
# async def lifespan():
#     await check_and_create_tables()

@app.get("/v1/healthcheck")
async def healthcheck():
    return {"status": "Healthy!"}


@app.get("/v1/students", response_model=List[StudentResponse])
async def get_students(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(10),  # Default limit is 10, must be >= 1
    offset: int = Query(0),   # Default offset is 0, must be >= 0
):
    # Validate the limit
    if limit < 1:
        raise HTTPException(status_code=400, detail="Limit must be greater than or equal to 1")
    # Validate the offset
    if offset < 0:
        raise HTTPException(status_code=400, detail="Offset must be greater than or equal to 0")

    try:
        # Build the base query
        query = select(Student).limit(limit).offset(offset)

        # Execute the query
        result = await db.execute(query)
        students = result.scalars().all()

        return students

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving students: {str(e)}")

@app.post("/v1/students", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_student = Student(
            first_name=student.first_name,
            last_name=student.last_name,
            email=student.email,
            date_of_birth=student.date_of_birth
        )
        db.add(new_student)
        await db.commit()  # Commit the transaction
        await db.refresh(new_student)  # Refresh to get the new ID
        return new_student
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating student: {str(e)}")


@app.get("/v1/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    try:
        # Query the database for the student by ID
        result = await db.execute(select(Student).where(Student.id == student_id))
        student = result.scalar_one_or_none()  # Returns None if no student found

        if student is None:
            raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")

        return student
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving student: {str(e)}")


@app.put("/v1/students/{student_id}", response_model=StudentResponse)
async def update_student(
        student_id: int,
        student_update: StudentUpdate,
        db: AsyncSession = Depends(get_db),
):
    # Check if the student exists
    student = await db.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check if the new email is unique
    if student_update.email:
        email_exists_query = select(Student).filter(Student.email == student_update.email)
        email_exists_result = await db.execute(email_exists_query)
        existing_student = email_exists_result.scalars().first()

        if existing_student and existing_student.id != student_id:
            raise HTTPException(status_code=400, detail="Email already exists")

    # Update the student record
    stmt = (
        update(Student)
        .where(Student.id == student_id)
        .values(
            first_name=student_update.first_name,
            last_name=student_update.last_name,
            email=student_update.email,
            date_of_birth=student_update.date_of_birth
        )
    )

    await db.execute(stmt)
    await db.commit()

    # Fetch the updated student record to return
    updated_student = await db.get(Student, student_id)
    return updated_student


@app.delete("/v1/students/{student_id}", response_description="Delete a student")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    # Check if the student exists
    query = select(Student).where(Student.id == student_id)
    result = await db.execute(query)
    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Store the student's details to return them later
    student_data = {
        "id": student.id,
        "first_name": student.first_name
    }

    # Delete the student
    await db.delete(student)
    await db.commit()

    return {"detail": "Student deleted successfully", "student": student_data}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
