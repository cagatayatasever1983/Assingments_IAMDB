from testhelpers import post_api, get_api, delete_api

class TestMovie(object):

# I am going to test GET REQUEST with different type of scenarios
    def test_get_all_movies(self):   
        status_code, data = get_api('movies')
        assert status_code == 200
        assert isinstance(data, list), "Response should be a list"
        assert len(data) > 0, "List of movies should not be empty"


    def test_get_movie_by_valid_id(self):
        known_id = '1232323'
        status_code, data = get_api(f'movies/{known_id}')
        assert status_code == 200
        assert data['id'] == known_id, "The movie ID should match the requested ID"
       
    def test_get_movie_by_invalid_id(self):
        non_existing_id = '@@@@@@'
        status_code, data = get_api(f'movies/{non_existing_id}')
        assert status_code == 404
        assert data == 'No movies found', "Response message should indicate no movies found"

    def test_get_movie_by_id_wrong_data_type(self):
        invalid_id = '@#23'
        status_code, _ = get_api(f'movies/{invalid_id}')
        assert status_code == 400 or status_code == 404, "Should return 400 Bad Request or 404 Not Found for invalid ID types"

# I am going to test POST REQUEST with valid information
        
def test_post_movie_with_valid_data(self):
        movie_data = {
            'title': 'Inception',
            'year': 2010
        }
        status_code, data = post_api('movies', movie_data)
        assert status_code == 201, "Status code should be 201 Created"
        assert 'id' in data, "Response should include an 'id' for the new movie"
        assert data['title'] == movie_data['title'], "The movie title should match the request"
        assert data['year'] == movie_data['year'], "The movie year should match the request"      

#I am going to test POST REQUEST with missing information
        
def test_post_movie_missing_required_field(self):
        movie_data = {
            'year': 2010
        }
        status_code, data = post_api('movies', movie_data)
        assert status_code == 400, "Status code should be 400 Bad Request"
        assert 'Missing required field title' in data, "Response should indicate the missing 'title' field"

#Testing POST REQUEST with the invalid date format
        
def test_post_movie_missing_required_field(self):
        # Prepare a request payload missing the 'title' field
        movie_data = {
            'year': 2010
        }
        
        # Make a POST request to the API
        status_code, data = post_api('movies', movie_data)
        
        # Assert that the API returns a 400 status code for a bad request
        assert status_code == 400, "Status code should be 400 Bad Request"
        
        # Assert that the response indicates the missing required field
        assert 'Missing required field title' in data, "Response should indicate the missing 'title' field"

#I am going to update an existing movie succesfully
def test_update_movie_with_valid_id(self):
        known_id = 'existing_movie_id'
        update_data = {
            'title': 'Updated Title',
            'year': 2021
        }
        status_code, data = put_api(f'movies/{known_id}', update_data)
        assert status_code == 200, "Status code should be 200 OK"
        assert data['title'] == update_data['title'], "Movie title should be updated"
        assert data['year'] == update_data['year'], "Movie year should be updated"

#I am going to create non-existing id ,GET REQUEST for all movie to be sure it is non-existing number
def test_update_non_existing_movie_creates_new(self):
        non_existing_id = 'non_existing_movie_id'
        new_movie_data = {
            'title': 'New Movie',
            'year': 2022
        }   
        status_code, data = put_api(f'movies/{non_existing_id}', new_movie_data)
        assert status_code == 201, "Status code should be 201 Created for a new movie"
        assert 'id' in data, "Response should include an 'id' for the new movie"
        assert data['title'] == new_movie_data['title'], "New movie title should match the request"
        assert data['year'] == new_movie_data['year'], "New movie year should match the request"

#with the below PUT REQUEST,I am going to update nonexisting field
def test_update_movie_with_invalid_field(self):
        known_id = 'existing_movie_id'
        update_data = {
            'title': 'Updated Title',
            'genre': 'Sci-Fi'  # Assuming 'genre' is not a valid field for a movie
        }
        status_code, data = put_api(f'movies/{known_id}', update_data)
        assert status_code == 200, "Status code should be 200 OK"
        assert 'genre' not in data, "Invalid fields should not be included in the response"

