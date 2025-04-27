from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the QR Event Check-in API!"}
    