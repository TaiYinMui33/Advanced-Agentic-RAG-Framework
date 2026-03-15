from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from services.rag_agent import AgenticRAGService
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
rag_service = AgenticRAGService()

class QueryRequest(BaseModel):
    query: str
    session_id: str = "default"

class QueryResponse(BaseModel):
    answer: str
    sources: list

@app.get("/")
def read_root():
    return {"status": "Online", "service": settings.PROJECT_NAME}

@app.post("/api/v1/query", response_model=QueryResponse)
async def query_rag_agent(request: QueryRequest):
    try:
        response, sources = await rag_service.process_query(request.query, request.session_id)
        return QueryResponse(answer=response, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
