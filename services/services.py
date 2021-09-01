from fastapi import FastAPI, webSocket 

@app.websocket("/ws")
async def websocket_endpoint(websocket :WebSocket):
    await websocket.accept()
    while True :
        data = await websocket.recive_text()
        awaut websocket.send_text(f"")