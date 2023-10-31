import xmlrpc.client
url = "http://localhost:8069"
db = "courses"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

#authentication
uid = common.authenticate(db, username, password, {})

if uid:
    print("authentication succeeded")

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # search methods
    partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]],
                                 {'limit': 5})

    # search count
    partners_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
    print("partners count = ", partners_count)

    # read methods
    partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners], {'fields': ['id', 'name']})

    # search read
    partner_rec2 = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['id', 'name']})
    print(">>>>>>",partner_rec2)


    #create record
    vals = {
        "name": "new external api",
        "email": "newexternalapi@gmail"
    }
    created_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
    print("created record >>", created_id)




else:
    print("authentication failed")
