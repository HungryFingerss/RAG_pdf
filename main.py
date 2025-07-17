from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from utlis import extract_text_from_pdf, chunk_text
from rag_engine import RAGPipeline

app = FastAPI()

rag_pipeline = None  # Global variable to hold the initialized pipeline


@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...), api_key: str = Form(...)):
    global rag_pipeline

    text = extract_text_from_pdf(file)
    chunks = chunk_text(text)

    rag_pipeline = RAGPipeline(api_key)
    rag_pipeline.index_chunks(chunks)

    return {
        "message": "PDF uploaded and indexed successfully.",
        "num_chunks": len(chunks)
    }


@app.post("/ask/")
async def ask_question(query: str = Form(...)):
    global rag_pipeline

    if not rag_pipeline:
        return JSONResponse(content={"error": "No document uploaded yet."}, status_code=400)

    result = rag_pipeline.ask(query)
    return {"query": query, "answer": result}
