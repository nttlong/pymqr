import datetime
class BaseObject(object):
    def __init__(self):
        self.Code = str,True
        self.Name = str, True
        self.FName = str,True
        self.Description = str
        self.CreatedBy = str, True
        self.CreatedOn = datetime.datetime,True
    def test(self):
        x=1

