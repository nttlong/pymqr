# -*- coding: utf-8 -*-

from pymqr import documents
from ..commons import BaseObject
@documents.Collection("departments")
@documents.UniqueIndex([
    "Code"
],[
    "LevelCode"
])
class Deps(BaseObject):
    def __init__(self):

        self.Level = int,True
        self.Alias = str,True
        self.ParentCode =str,True
        self.LevelCode = [str]
        super(type(self), self).__init__()





# department_code=helpers.create_field("text", True),
#             #parent_id=helpers.create_field("numeric"),
#             parent_code=helpers.create_field("text"),
#             level=helpers.create_field("numeric"),
#             level_code=helpers.create_field("text"),
#             level_code2=helpers.create_field("text"),
#             department_tel=helpers.create_field("text"),
#             department_fax=helpers.create_field("text"),
#             department_email=helpers.create_field("text"),
#             department_address=helpers.create_field("text"),
#             #Xem lại kiểu dữ liệu
#             nation_code=helpers.create_field("text"),
#             province_code=helpers.create_field("text"),
#             district_code=helpers.create_field("text"),
#             is_company=helpers.create_field("bool"),
#             is_fund=helpers.create_field("bool"),
#             is_fund_bonus=helpers.create_field("bool"),
#             decision_no=helpers.create_field("text"),
#             decision_date=helpers.create_field("date"),
#             effect_date=helpers.create_field("date"),
#             license_no=helpers.create_field("text"),
#             tax_code=helpers.create_field("text"),
#             lock_date=helpers.create_field("date"),
#             logo_image=helpers.create_field("text"),
#             manager_code=helpers.create_field("text"),
#             secretary_code=helpers.create_field("text"),
#             ordinal=helpers.create_field("text"),
#             lock=helpers.create_field("bool"),
#             note=helpers.create_field("text"),
#             region_code=helpers.create_field("text"),
#             domain_code=helpers.create_field("text"),
#             signed_by=helpers.create_field("text"),
#             created_on=helpers.create_field("date"),
#             created_by=helpers.create_field("text"),
#             modified_on=helpers.create_field("date"),
#             modified_by=helpers.create_field("text")