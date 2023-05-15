from pymongo import mongo_client

MONGO_DB_CONNECTION_URI = "mongodb://localhost:27017"

client = mongo_client.MongoClient(MONGO_DB_CONNECTION_URI)
print("Connected to MongoDB")

# Get or create database
BookDB = client["BookDB"]
