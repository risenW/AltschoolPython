from pymongo import mongo_client
from utils import logger

MONGO_DB_CONNECTION_URI = "mongodb://localhost:27017"

client = mongo_client.MongoClient(MONGO_DB_CONNECTION_URI)
logger.info("Connected to MongoDB successfully")

# Get or create collection
accounts_collection = client["bankapp"]["accounts"]
users_collection = client["bankapp"]["users"]

