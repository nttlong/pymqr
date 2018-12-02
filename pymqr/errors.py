import pymongo
__index_info__ = None
import threading
lock = threading.Lock()
class DataException(Exception):
    def __init__(self, message, errors):
        self.fields = errors.get("fields",[])
        self.index_name = errors.get("index","")
        self.collection_name =  errors.get("collection_name","")
        self.code = errors.get("code",0)


        # Call the base class constructor with the parameters it needs
        super (DataException, self).__init__ (message)
        # Now for your custom code...
        self.errors = errors
def __duplicate__(coll,ex):
    import inspect
    if isinstance(ex,pymongo.errors.DuplicateKeyError):
        global __index_info__
        if __index_info__ == None:
            __index_info__ = {}
        index_name = ex.message.split (':')[2].rstrip (' ').lstrip (' ').split (' ')[0].rstrip (' ').lstrip (' ')

        if isinstance(coll,pymongo.mongo_client.database.Collection):
            if not __index_info__.has_key(coll.name):
                lock.acquire()
                try:
                    __index_info__.update({
                        coll.name:coll.index_information()
                    })
                    lock.release()

                except Exception as ex:
                    lock.release()
            index = __index_info__[coll.name]
            return DataException(ex.message,dict(
                collection_name=coll.name,
                code=ex.code,
                index = index_name,
                fields = [x[0] for x in index[index_name]["key"]]
            ))
        else:
            raise Exception("The first param must be '{0}'".format(
                pymongo.mongo_client.database.Database
            ))
