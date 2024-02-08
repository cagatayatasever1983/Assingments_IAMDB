from flask import Flask
from flask_restful import Api, Resource, reqparse
from Movie import Movie
from Person import Person
from Search import Search

app = Flask(__name__)
api = Api(app)

api.add_resource(Movie, '/movies/', '/movies/<string:id>')
api.add_resource(Person, '/persons/', '/persons/<string:id>')
api.add_resource(Search, '/search/<string:query>')

app.run(debug=True, port="8002")
