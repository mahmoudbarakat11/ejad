import xmlrpc.client
url = "http://localhost:8069"
db = "courses"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print(version)

uid = common.authenticate(db, username, password, {})
print(">>>>>", uid)

#search
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
partners_ids = models.execute_kw(db, uid, password, 'res.partner', 'search',[[]],{'offset':10,'limit':5})
print("partners>>>", partners_ids)

#search count
partners_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count',[[]])
print("partners count>>>>>>>>", partners_count)

#read
partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners_ids],{'fields':['id','name']})
for rec in partner_rec:
    print(rec)

#search read
partner_rec2 =models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[]], {'fields': ['id','name']})
for rec in partner_rec2:
    print(rec)

#create record
new_contact = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner","mobile":"1234","website":"test"}])
print(">>...",new_contact)





