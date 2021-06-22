from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
   
    def _init_(self, username, password):
         """ Initializing the MongoClient. This helps to access the Mongo
         databases and collections """
         self.client = MongoClient ('mongodb://%s:%s@localhost:33369' % (username,password))
         self.database = self.client['AAC']
        
    def create(self, data = None) -> bool:
        """process to create a new entry, will need to pass a dict object that matches entries in the database"""
        if data is not None:
           run = self.database.animals.insert(data)
           if run != 0:
                return True
           else:
                return False
        else:
            raise Exception('Nothing to save, because data parameter is empty')
            
    def read(self, data = None) -> dict:
                """process to read an entry, will need to pass a dict object that matches entries in the database"""
                if data is not None:
                    run = self.database.animals.find(data,{"_id": False})
                    if run != 0:
                        response = run
                    else:
                        response = "unable to find result."
                else:
                    "raise Exception('Nothing to show, because data parameter is empty')"
   
                return response
    
    def update(self, searchData = None, updateData = None):
                """process to update an existing entry, will need to pass a dict objects that matches entries in the database"""

                if searchData is not None:
                    run = self.database.animals.update(searchData, updateData)
                    if run != 0:
                        response = run
                    else:
                        response = "unable to add field to database."
                else:
                    raise Exception('One or more data parameters are blank')
                return response
    
    def delete(self, data = None):
                """process to delete an entry, will need to pass a dict object that matches entries in the database"""
                if data:
                    run = self.database.animals.remove(data)
                    if run != 0:
                        response = run
                    else:
                        response = "unable to process delete request at this time"
                else:
                    raise Exception('Nothing to delete because data parameter is empty')
                return response
    


