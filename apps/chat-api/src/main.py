"""自研 Chat API: 全项目唯一手写服务, 每行都要能讲。
链路: 请求 -> Redis读会话 -> (TODO RAG检索) -> 调 vLLM -> 写审计 -> 返回
"""
import os, time, json, logging
import httpx
from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator

VLLM = os.getenv("VLLM_BASE_URL", "http://vllm-router-service.inference/v1")
MODEL = os.getenv("MODEL_NAME", "facebook/opt-125m")   # TODO(你来改): 与 inference values 一致

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger("chat")
app = FastAPI()
Instrumentator().instrument(app).expose(app)   # /metrics

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.post("/v1/chat")
async def chat(req: Request):
    body = await req.json()
    user = req.headers.get("x-user-id", "anonymous")   # 网关鉴权后注入
    t0 = time.time()
    # TODO(阶段4): Redis 会话读写; Milvus/pgvector 检索并拼接 system prompt
    async with httpx.AsyncClient(timeout=120) as cli:
        r = await cli.post(f"{VLLM}/chat/completions", json={
            "model": MODEL,
            "messages": body.get("messages", []),
            "max_tokens": body.get("max_tokens", 256),
        })
    data = r.json()
    usage = data.get("usage", {})
    # 结构化日志: 这是 Loki 里排障与成本分析的原材料
    log.info(json.dumps({
        "event": "chat", "user": user, "model": MODEL,
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "latency_ms": int((time.time()-t0)*1000), "status": r.status_code,
    }))
    # TODO(阶段4): 审计落 PostgreSQL
    return data
