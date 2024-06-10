import uuid
import bcrypt
import datetime
from fastapi import HTTPException
from app.database.db import database
from app.utils.email import send_email

class UserService:
    async def create_user(self, email: str, password: str):
        user_id = str(uuid.uuid4())
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        query = """
        INSERT INTO users (id, email, password, is_active, created_at, updated_at)
        VALUES (:id, :email, :password, :is_active, :created_at, :updated_at)
        """
        values = {
            "id": user_id,
            "email": email,
            "password": hashed_password,
            "is_active": False,
            "created_at": datetime.datetime.utcnow(),
            "updated_at": datetime.datetime.utcnow()
        }
        await database.execute(query, values)

class VerificationService:
    async def send_code(self, email: str):
        user_query = "SELECT id FROM users WHERE email = :email"
        user = await database.fetch_one(user_query, {"email": email})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        code = str(uuid.uuid4())[:4]
        verification_id = str(uuid.uuid4())
        query = """
        INSERT INTO verification_codes (id, user_id, code, created_at)
        VALUES (:id, :user_id, :code, :created_at)
        """
        values = {
            "id": verification_id,
            "user_id": user["id"],
            "code": code,
            "created_at": datetime.datetime.utcnow()
        }
        await database.execute(query, values)

        # Mock email sending
        send_email(email, code)

    async def activate_user(self, email: str, code: str):
        user_query = "SELECT id FROM users WHERE email = :email"
        user = await database.fetch_one(user_query, {"email": email})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        code_query = "SELECT * FROM verification_codes WHERE user_id = :user_id AND code = :code"
        verification = await database.fetch_one(code_query, {"user_id": user["id"], "code": code})
        if not verification:
            raise HTTPException(status_code=400, detail="Invalid code")

        current_time = datetime.datetime.utcnow()
        code_time = verification["created_at"]
        if (current_time - code_time).total_seconds() > 60:
            raise HTTPException(status_code=400, detail="Code expired")

        update_query = "UPDATE users SET is_active = TRUE WHERE id = :id"
        await database.execute(update_query, {"id": user["id"]})
