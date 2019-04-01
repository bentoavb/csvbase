from csvbase import CSVbase

db = CSVbase("db")

db.createTable('exampleTable3',['c1','c2','c3'])

db.create('exampleTable3', {
    'c1': 'x',
    'c2': 'y',
    'c3': 'z'
})

db.create('exampleTable3', {
    'c1': '1',
    'c2': '2',
    'c3': '3'
})

print('before delete: ', db.read('exampleTable3'))

db.delete('exampleTable3',{
    # condition for select a row for delete
    'c1': '1',
    'c2': '2'
})

print('after delete:', db.read('exampleTable3'))
