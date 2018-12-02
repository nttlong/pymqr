import pymongo
class DataException(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super (DataException, self).__init__ (message)
        # Now for your custom code...
        self.errors = errors
def __duplicate__(db,coll_name,ex):
    import inspect
    if isinstance(ex,pymongo.errors.DuplicateKeyError):
        index_name = ex.message.split (':')[2].rstrip (' ').lstrip (' ').split (' ')[0].rstrip (' ').lstrip (' ')
        if isinstance(db,pymongo.mongo_client.database.Database):
            index = db.get_collection(coll_name).index_information()
            return DataException(ex.message,dict(
                collection_name=coll_name,
                code=ex.code,
                index = index
            ))
        else:
            raise Exception("The first param must be '{0}'".format(
                pymongo.mongo_client.database.Database
            ))
