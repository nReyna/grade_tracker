from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')

grades = client.tracker.grades

# for _ in range(3):
#     name = input('Student Name:')
#     klass = input('Student Class:')
#     grade = float(input('Grade:'))

#     d = {'name': name, 'class': klass, 'grade': grade}
#     grades.insert_one(d)

total = 0
count = grades.find().count()
for g in grades.find():
    # print('g is', g)
    # print('g is', g['grade'])
    total += g['grade']
print(total/count)

print(grades.count())
print(grades.find().count())
print(len(grades))