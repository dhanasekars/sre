from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/v1/healthcheck")
async def healthcheck():
    return JSONResponse(content={"status": "up and running"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
