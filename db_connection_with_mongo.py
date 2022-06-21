import pymongo

# mongodb cluster URl
connectionString = "mongodb+srv://Shubh:<password>@cluster0.tt98tdj.mongodb.net/test"

# create database and inset id
if __name__ == '__main__':
    client = pymongo.MongoClient(connectionString)
    db = client['test-database']
    # collection = db['test-collection']

    posts = db.posts
    post_id = posts.insert_one({"p": 1}).inserted_id
    print(post_id)

    # For checking database exist or not
    dblist = client.list_database_names()
    if "test-database" in dblist:
        print("The database exists.")
