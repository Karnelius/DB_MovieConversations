# 27027

from pymongo import MongoClient


def main():
    client = MongoClient('mongodb://root:s3cr37@localhost:27027')
    db = client.person_db
    persons_collection = db.persons
    p1 = {
        'first_name': "David",
        'last_name': "Karnel",
        'age': 33,
        'likes': ['Candles', 'Walks', 'Dogs']
    }
    p2 = {
        'first_name': "Lisa",
        'last_name': "Andersson",
        'age': 23,
        'fav_music': "Punk"
    }

    # p1_id = persons_collection.insert_one(p1).inserted_id
    p1['_id'] = persons_collection.insert_one(p1).inserted_id
    p2['_id'] = persons_collection.insert_one(p2).inserted_id

    # p2_id = persons_collection.insert_one(p2).inserted_id

    print(p1)
    print(p2)


if __name__ == '__main__':
    main()
