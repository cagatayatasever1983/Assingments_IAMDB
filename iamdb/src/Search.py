from flask_restful import Resource
from requesthelpers import load_db

class Search(Resource):
    def get(self, query):
        terms = query.lower().split('-')
        db = load_db('person') + load_db('movie')
        result = []
        for item in db:
            for key in item:
                if isinstance(item[key], str) and key != 'id':
                    for term in terms:
                        if term in item[key].lower():
                            result.append(item)
        
        return ('No results', 404) if (len(result) < 1) else result
