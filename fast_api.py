import my_module
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
async def root():
    new = my_module.uid_generate()
    return new


uvicorn.run(app)