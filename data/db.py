from motor.motor_asyncio import AsyncIOMotorClient
from config import config

client = AsyncIOMotorClient(
    config.MONGODB_URI,
    ssl=True,
    tlsAllowInvalidCertificates=True)
resume_db = client.resumeDB
red_ribbon_db = client.redRibbon