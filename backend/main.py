# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="墨灵 - AI 小说助手", version="1.0.0")

# 允许前端跨域请求（开发时需要）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "墨灵后端已启动！V1 开发中...", "status": "ok"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "moe-ling-backend"}