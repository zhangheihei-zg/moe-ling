# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# 👇 关键：将项目根目录加入 Python 路径（确保能导入 backend.*）
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# 导入路由（必须放在路径设置之后）
from backend.routers.novel import router as novel_router

app = FastAPI(
    title="墨灵 V1 API",
    description="AI 小说创作助手后端服务",
    version="0.1.0"
)

# CORS 配置（允许前端跨域）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应限制为具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 健康检查
@app.get("/")
async def root():
    return {"message": "欢迎使用「墨灵」AI 小说创作平台！"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

# 👇 注册小说路由
app.include_router(novel_router)