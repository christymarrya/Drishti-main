from backend_api import app
from fastapi.responses import JSONResponse

@app.get("/")
def root():
    return JSONResponse({"status": "ok", "message": "DRISHTI API is running"})
