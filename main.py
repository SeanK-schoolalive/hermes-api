from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Hermes API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str
    context: str | None = None


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat")
async def chat(request: ChatRequest):
    prompt = request.prompt
    context = request.context or ""

    # Placeholder integration point for actual Hermes logic.
    # Replace this with your Hermes runtime invocation when ready.
    reply = f"Echo from Hermes API: {prompt}"

    return {
        "reply": reply,
        "prompt": prompt,
        "context": context,
    }


@app.get("/")
async def root():
    return {"message": "Hermes API is running"}
