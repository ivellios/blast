from pymongo import MongoClient

class Mongo():

    def __init__(self, username, password, host, port):
        self._client = MongoClient('mongodb://{}:{}@{}:{}/blast_video'.format(username, password, host, port))

    def get(self, text):
        result = []
        collection = self._client.blast_video.video
        for obj in collection.find({'title': {'$regex': text}}):
            result.append(obj)
        return result
