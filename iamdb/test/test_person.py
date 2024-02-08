from testhelpers import post_api, get_api, delete_api

class TestPerson(object):
    def test_post_person_with_valid_data(self):
        new_person = {'first_name': 'Patrick', 'last_name': 'Stewart', 'birth_year': 1940}
        status_code, data = post_api('persons', new_person)
        assert status_code == 201
        assert data['first_name'] == 'Patrick'
        assert data['last_name'] == 'Stewart'
        assert data['birth_year'] == 1940
        assert isinstance(data['id'], str)

# With below codes,I want to check API status code when one of the required place is missing
        
def test_post_person_missing_first_name(self):
    incomplete_person = {'last_name': 'Stewart', 'birth_year': 1940}
    status_code, data = post_api('persons', incomplete_person)
    assert status_code == 400
    assert 'Missing required field first_name' in data

def test_post_person_missing_last_name(self):
    incomplete_person = {'first_name': 'Patrick', 'birth_year': 1940}
    status_code, data = post_api('persons', incomplete_person)
    assert status_code == 400
    assert 'Missing required field last_name' in data

def test_post_person_missing_birth_year(self):
    incomplete_person = {'first_name': 'Patrick', 'last_name': 'Stewart'}
    status_code, data = post_api('persons', incomplete_person)
    assert status_code == 400
    assert 'Missing required field birth_year' in data

#It is import to test API status code with invalid value.
# I am assuming that firstname and lastname is String and birthyear is integer
    
def test_post_person_with_invalid_birth_year(self):
    new_person = {'first_name': 'Patrick', 'last_name': 'Stewart', 'birth_year': 'nineteen forty'}
    status_code, data = post_api('persons', new_person)
    assert status_code == 400
    assert 'Invalid data type for birth_year' in data  # I am expecting to see this message lets say based on swagger 


def test_post_person_with_invalid_first_name(self):
    new_person = {'first_name': 1234, 'last_name': 'Stewart', 'birth_year': 1940}
    status_code, data = post_api('persons', new_person)
    assert status_code == 400
    assert 'Invalid data type or format for first_name' in data  # I can change this message based on what is written in swagger

def test_post_person_with_invalid_last_name(self):

    new_person = {'first_name': 'Patrick', 'last_name': '@Stewart!', 'birth_year': 1940}
    status_code, data = post_api('persons', new_person)
    assert status_code == 400
    assert 'Invalid data type or format for last_name' in data  # I can change this message based on what is written in swagger


#To test GET request I have generated below but what i liked to do generate a method to produce non-existing number
#the method for non existing number help me to find which number is not in the first get call
    
def test_get_all_persons(self):
        status_code, data = get_api('persons')
        assert status_code == 200
        assert isinstance(data, list)  # Assuming the data is returned as a list


#After running first Get method I can get the first id number to run the below 
def test_get_person_by_valid_id(self):
        status_code, data = get_api('persons/123')
        assert status_code == 200
        assert data['id'] == '123'

#I can run the nonexisting number method to create number
#after finding nonexisting number,I can run this get request method
def test_get_person_by_invalid_id(self):
        status_code, data = get_api('persons/nonexistent_id')
        assert status_code == 404
        assert data == 'No persons found'



#I assume that id=123 is in the database
def test_put_person_with_valid_data(self):
        updated_person = {'first_name': 'Ian', 'last_name': 'McKellen'}
        status_code, data = put_api('persons/123', updated_person)
        assert status_code == 200
        assert data['first_name'] == 'Ian'
        assert data['last_name'] == 'McKellen'


#I have to be sure there is an existing person to update 
def test_put_update_with_invalid_field(self):
    existing_person = {'first_name': 'James', 'last_name': 'Kirk', 'birth_year': 2233}
    post_status_code, post_data = post_api('persons', existing_person)
    assert post_status_code == 201

#I try to update the person with nonexisting field
    update_data = {'rank': 'Captain'}
    put_status_code, put_data = put_api(f'persons/{post_data["id"]}', update_data)
    assert put_status_code == 400  # I can change this line based on swagger
    assert 'Invalid field' in put_data  


#Firstly generate nonexistig number and use get request method to see whether it is in database or not
def test_put_update_non_existing_creates_new(self):
    new_person_data = {'first_name': 'Spock', 'last_name': 'Only', 'birth_year': 2230}
    put_status_code, put_data = put_api('persons/non_existing_id', new_person_data)
    assert put_status_code == 201 #this part is depends on backend developer how they handle this scenario.It can be 400
    assert 'id' in put_data  # Check if a new ID was assigned

#First I make a post request to create a person ,after being sure there is an existing person.I can do put request
def test_put_update_existing_person(self):
    existing_person = {'first_name': 'Jean-Luc', 'last_name': 'Picard', 'birth_year': 2305}
    post_status_code, post_data = post_api('persons', existing_person)
    assert post_status_code == 201

#updating 
    update_data = {'first_name': 'Jean-Luc', 'last_name': 'Picard', 'birth_year': 2306}
    put_status_code, put_data = put_api(f'persons/{post_data["id"]}', update_data)
    assert put_status_code == 200
    assert put_data['birth_year'] == 2306  # Check if the birth year was updated correctly

 # I am assuming a person with ID '123' exists and can be deleted
def test_delete_person_with_valid_id(self):
        status_code, data = delete_api('persons/123')
        assert status_code == 200
        assert data == "Person successfully deleted"
        
 # I am deleting nonexisting person
def test_delete_person_with_invalid_id(self):
        status_code, data = delete_api('persons/nonexistent_id')
        assert status_code == 404
        assert data == "Person not found"

