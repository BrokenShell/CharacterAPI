import datetime
from os import getenv
from typing import Optional, List, Dict, Iterator

from pymongo import MongoClient
from dotenv import load_dotenv


class MongoDB:
    load_dotenv()

    def __init__(self, database: str):
        self.database = database

    def connect(self, collection: str):
        return MongoClient(getenv("MONGO_URL"))[self.database][collection]

    def create(self, collection: str, data: Dict) -> bool:
        return self.connect(collection).insert_one(
            document=timestamp(data),
        ).acknowledged

    def create_many(self, collection: str, data: Iterator[Dict]) -> bool:
        return self.connect(collection).insert_many(
            documents=map(timestamp, data),
        ).acknowledged

    def read(self, collection: str, query: Optional[Dict] = None) -> List[Dict]:
        return list(self.connect(collection).find(
            filter=query,
            projection={"_id": False},
        ))

    def update(self, collection: str, query: Dict, update_data: Dict) -> bool:
        update_data["updated_at"] = datetime.datetime.now()
        return self.connect(collection).update_many(
            filter=query,
            update={"$set": update_data},
        ).acknowledged

    def delete(self, collection: str, query: Dict) -> bool:
        return self.connect(collection).delete_many(
            filter=query,
        ).acknowledged

    def count(self, collection: str, query: Optional[Dict] = None) -> int:
        return self.connect(collection).count_documents(
            filter=query or {},
        )


def timestamp(data: Dict) -> Dict:
    data["created_at"] = datetime.datetime.now()
    return data
