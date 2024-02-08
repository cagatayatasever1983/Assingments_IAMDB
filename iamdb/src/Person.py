from flask import request
from flask_restful import Resource
import uuid
from requesthelpers import get_item_from_db_by_id, delete_from_db_by_id, load_db, save_db

class Person(Resource):
    def get(self, id=None):
        result = None
        if id == None:
            result = load_db('person')
        else:
            result = get_item_from_db_by_id(id, 'person')
        return ('No persons found', 404) if result == None else (result, 200)

    def post(self):
        data = request.json

        required_fields = ['first_name', 'last_name', 'birth_year']
        for field in required_fields:
            if field not in data:
                return 'Missing required field {0}'.format(field), 400

        person = {
            'id': str(uuid.uuid4()),
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'birth_year': data['birth_year'],
        }

        persons = load_db('person')
        persons.append(person)
        save_db(persons, 'person')

        return person, 201

    def put(self, id):
        persons = load_db('person')
        for idx, person in enumerate(persons):
            if person['id'] == id:
                data = request.json
                for key in data:
                    if key in person:
                        persons[idx][key] = data[key]
                save_db(persons, 'person')
                return person
        return self.post()

    def delete(self, id):
        result = delete_from_db_by_id(id, 'person')
        return ("Person successfully deleted", 200) if result == True else ("Person not found", 404)