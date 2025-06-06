from fastapi import FastAPI, HTTPException, Header, Depends
from typing import Optional
import httpx

app = FastAPI()

SECRET_PASSWORD = "766"
RAWG_API_KEY = "a01c35a177e5403ea74e703f3e0d1ba5"

def verify_password(x_api_key: Optional[str] = Header(None)):
    if x_api_key != SECRET_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

async def fetch_metacritic_score(game_name: str) -> Optional[int]:
    url = f"https://api.rawg.io/api/games"
    params = {
        "key": RAWG_API_KEY,
        "search": game_name,
        "page_size": 1,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            game = data["results"][0]
            return game.get("metacritic")
        return None

@app.get("/game-score")
async def get_game_score(game_name: str, authorized: bool = Depends(verify_password)):
    score = await fetch_metacritic_score(game_name)
    if score is None:
        raise HTTPException(status_code=404, detail="Game not found or no Metacritic score")
    return {"game": game_name, "metacritic_score": score}
