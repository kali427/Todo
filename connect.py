import pymongo
import os


# for cloud database
# from dotenv import load_dotenv
# load_dotenv()
# username = os.getenv('USER')
# password = os.getenv('PASSWORD')
# client = pymongo.MongoClient(f"mongodb://{username}:{password}@ac-fkcbfze-shard-00-00.plpcgc2.mongodb.net:27017,ac-fkcbfze-shard-00-01.plpcgc2.mongodb.net:27017,ac-fkcbfze-shard-00-02.plpcgc2.mongodb.net:27017/?ssl=true&replicaSet=atlas-fdj15p-shard-0&authSource=admin&retryWrites=true&w=majority")

# for local database 
client = pymongo.MongoClient(f"mongodb://localhost:27017")
db = client.todo

todos = db['todos']