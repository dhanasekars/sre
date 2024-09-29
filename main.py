from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db
from models import Student

app = FastAPI()

@app.get("/v1/healthcheck")
async def healthcheck():
    return {"status": "Healthy!"}

@app.get("/v1/students")
async def get_students(db: AsyncSession = Depends(get_db)):
    try:
        # Query the students table
        result = await db.execute(select(Student))
        students_list = result.scalars().all()

        if not students_list:
            raise HTTPException(status_code=404, detail="No students found")

        # Return the list of students
        return students_list

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving students: {str(e)}")




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
