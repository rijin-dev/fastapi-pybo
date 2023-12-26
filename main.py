from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles


from domain.question import question_router
from domain.answer import answer_router



app = FastAPI()

origins = [
    "http://localhost:5173",
    #"http://127.0.0.1:5173",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/")
# def root():
#     return {"Hello": "World"}
#
#
# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))

@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")