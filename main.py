from fastapi import FastAPI
import uvicorn

from src.controllers.controller_routers import api_router

app = FastAPI(title='Food Order App',
              description='An Food Order App API Endpoints',
              docs_url='/food-app/v1/api/docs',
              redoc_url='/food-app/v1/api/redoc')


@app.get('/')
def home():
    return "Hello World"


app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8001, reload=True)
