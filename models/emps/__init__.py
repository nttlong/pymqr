from pymqr import documents
@documents.Collection("employees")
@documents.UniqueIndex([
    "Code"
],[
    "Email"
])
class Emps(object):
    def __init__(self):
        self.Code=str,True
        self.FirstName=str,True
        self.LastName=str,True

