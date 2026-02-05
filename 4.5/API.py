from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import bcrypt
import jwt
from datetime import datetime, timedelta

# ================= КОНФІГ =================
SECRET_KEY = "supersecretkey123"  # для підпису JWT
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ================= ДАНІ =================
# Приклад "бази користувачів" у пам'яті
users_db = {}

# ================= СХЕМИ =================
class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ================= FASTAPI =================
app = FastAPI(title="JWT Auth Demo")

# ================= ХЕЛПЕРИ =================
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ================= РЕЄСТРАЦІЯ =================
@app.post("/register")
def register(user: UserRegister):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed = hash_password(user.password)
    users_db[user.username] = {"password": hashed}
    return {"status": "success", "message": "User registered"}

# ================= ЛОГІН =================
@app.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    db_user = users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token}

# ================= ПРОФІЛЬ =================
@app.get("/profile")
def profile(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    username = payload.get("sub")
    return {"status": "success", "data": {"username": username}, "message": "Profile data"}

# ================= ДЕМОНСТРАЦІЯ =================
@app.get("/")
def root():
    return {"message": "JWT Auth Demo. Зареєструйся та залогінься для отримання токена."}