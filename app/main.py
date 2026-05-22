from fastapi import FastAPI

app = FastAPI(
    title="AI Crypto Testnet Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Crypto Testnet Platform Running"
    }