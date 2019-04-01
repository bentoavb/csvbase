from csvbase import CSVbase

db = CSVbase("db")

db.createTable('exampleTable1',['c1','c2','c3'])

db.create('exampleTable1', {
    'c1': '1',
    'c2': '2',
    'c3': '3'
})

db.create('exampleTable1', {
    'c1': '4',
    'c2': '5',
    'c3': '6'
})

readAll = db.read('exampleTable1')

print('read all: ', readAll)

readWithCondition = db.read('exampleTable1',{
    # condition for select a row for read
    'c1': '4'
})

print('read with condition:', readWithCondition)
