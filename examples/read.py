from csvbase import CSVbase

db = CSVbase()

# create a file named exampleTable1.csv

db.createTable('exampleTable1',['c1','c2','c3'])

# insert data on the file exampleTable1.csv

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

# read all data of the file exampleTable1.csv

readAll = db.read('exampleTable1')
print('read all: ', readAll)

# read data with a condition 

readWithCondition = db.read('exampleTable1',{
    'c1': '4' # condition for select a row for read
})
print('read with condition:', readWithCondition)
