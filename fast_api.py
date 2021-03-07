from fastapi import FastAPI
import uvicorn
from starlette.responses import RedirectResponse


app = FastAPI()


@app.get("/shops")
async def get_shops():
    return [{"name": "COM7"}, {"name": "JIB"}, {"name": "ADVICE"}]

  
if __name__ == "__main__":
    uvicorn.run("fast_api:app", host="0.0.0.0", port=8080)
