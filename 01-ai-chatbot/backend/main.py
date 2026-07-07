from fastapi import FastAPI

app=FastAPI(title="Ai Chat Boat")
@app.get("/helth")
def helth_check():
    return {"status":"ok"}
