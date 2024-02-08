from flask import request
from flask_restful import Resource
import uuid
from requesthelpers import get_item_from_db_by_id, delete_from_db_by_id, load_db, save_db

class Movie(Resource):
    def get(self, id=None):
        result = None
        if id == None:
            result = load_db('movie')
        else:
            result = get_item_from_db_by_id(id, 'movie')
        return ('No movies found', 404) if result == None else (result, 200)

    def post(self):
        data = request.json

        required_fields = ['title', 'year']
        for field in required_fields:
            if field not in data:
                return 'Missing required field {0}'.format(field), 400

        movie = {
            'id': str(uuid.uuid4()),
            'title': data['title'],
            'year': data['year'],
        }

        movies = load_db('movie')
        movies.append(movie)
        save_db(movies, 'movie')

        return movie, 201

    def put(self, id):
        movies = load_db('movie')
        for idx, movie in enumerate(movies):
            if movie['id'] == id:
                data = request.json
                for key in data:
                    if key in movie:
                        movies[idx][key] = data[key]
                save_db(movies, 'movie')
                return movie
        return self.post()


    def delete(self, id):
        result = delete_from_db_by_id(id, 'movie')
        return ('Movie successfully deleted', 200) if result == True else ('Movie not found', 404)