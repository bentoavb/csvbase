from csvbase import CSVbase

db = CSVbase("db")

db.createTable('exampleTable4',['c1','c2','c3'])

print('before drop: ', db.listTables(extension=False))

db.dropTable('exampleTable4')

print('after drop: ', db.listTables(extension=False))
