from csvbase import CSVbase

db = CSVbase("db")

db.createTable('exampleTable2',['c1','c2','c3'])

db.create('exampleTable2', {
    'c1': 'a',
    'c2': 'b',
    'c3': 'c'
})

db.create('exampleTable2', {
    'c1': 'd',
    'c2': 'e',
    'c3': 'f'
})

print('before update: ', db.read('exampleTable2'))

db.update('exampleTable2',{
    # condition for select a row for update
    'c1': 'a',
    'c2': 'b'
},{
    # item to update
    'c2': 'item updated' ,
    'c3': 'other item updated'
})

print('after update:', db.read('exampleTable2'))
