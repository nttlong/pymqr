import models.emps as emp
import pymongo
from pymqr import query
from pymqr import settings
from models.categories import deps
cnn = pymongo.MongoClient(
    host = "localhost",
    port =27017
)
db = cnn.get_database("db1")
db.authenticate("root","123456")
settings.setdb(db)

data = deps.Deps<<{}
import pprint
pprint.pprint(data.to_dict())
