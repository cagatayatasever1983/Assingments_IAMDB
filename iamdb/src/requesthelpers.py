import json

def get_item_from_db_by_id(id, db_name):
    db = load_db(db_name)
    for item in db:
        if (item['id'] == id):
            return item
    return None

def delete_from_db_by_id(id, db_name):
    db = load_db(db_name)
    result = False
    for item in db:
        if item['id'] == id:
            db.remove(item)
            save_db(db, db_name)
            result = True
    return result

def load_db(db_name):
    with open('database/{0}.json'.format(db_name)) as f:
        return json.load(f)
    
def save_db(data, db_name):
    with open('database/{0}.json'.format(db_name), 'w+') as f:
        json.dump(data, f)
