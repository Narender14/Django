from pymongo import MongoClient

class Database(object):
    """Class for interacting with the FileMetadata mongo store"""

    def __init__(self,db_host='localhost', db_port=27017, db_name='twitter', db_collection_name='tweet', db_user='',
                 db_password=''):
        self.client, self.collection = None, None
        self.db_host = db_host
        self.db_port = int(db_port)
        self.db_name = db_name
        self.db_collection_name = db_collection_name
        self.db_user = db_user
        self.db_password = db_password

    def connect(self):

        """Make connection to MongoDB instance. Initialize the collection document.

        """

        self.client = MongoClient(self.db_host, self.db_port)
        self.collection = self.client[self.db_name][self.db_collection_name]

