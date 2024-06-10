from database import Database
from app.utils.config import DATABASE_URL
from app.database.models import CREATE_USERS_TABLE, CREATE_VERIFICATION_CODES_TABLE

database = Database(DATABASE_URL)

async def create_tables():
    await database.execute(CREATE_USERS_TABLE)
    await database.execute(CREATE_VERIFICATION_CODES_TABLE)
