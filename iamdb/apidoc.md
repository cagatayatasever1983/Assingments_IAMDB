# I am Db API documentation

Below is a reference guide for all the API endpoints supported by I am Db.

## Person

Persons include everyone who has contributed to a film stored in the I am Db database. 

### Available methods

### GET `/persons/{person_id}`

Retrieves the person with the specified id. If no id is provided, the entire persons database is returned. 

Sample response body:
```
{
    "id": "b9f2d28c-57dc-4381-a752-ac36611ab51a",
    "first_name": "Arnold",
    "last_name": "Schwarzenegger",
    "birth_year": 1947
}
```

### POST `/persons/`

Creates a new person in the database based on the json passed to the call. `first_name`, `last_name`, and `birth_year` are all required fields. When successful, the new person will be included in the response. 

Sample request body:
```
{
    "first_name": "Arnold",
    "last_name": "Schwarzenegger",
    "birth_year": 1947
}
```

Sample response body:
```
{
    "id": "b9f2d28c-57dc-4381-a752-ac36611ab51a",
    "first_name": "Arnold",
    "last_name": "Schwarzenegger",
    "birth_year": 1947
}
```

### PUT `/persons/{person_id}`

Will search the database for an id match and update the person based on the json passed. In this scenario, any combination of valid person properties can be updated at a time. If no person can be found, a new one will be created. If a new person is created, the request will be rejected if the json body does not include all required properties: `first_name`, `last_name`, and `birth_year`. The new/edited person will be returned in the response. 

Sample request body:
```
{
    "first_name": "Marcy"
}
```

Sample response body:
```
{
    "id": "b9f2d28c-57dc-4381-a752-ac36611ab51a",
    "first_name": "Marcy",
    "last_name": "Schwarzenegger",
    "birth_year": 1947
}
```

### DELETE `/persons/{person_id}`

Deletes the person with the specified id. 


## Movie

Movies refers to all movie entries stored in I am Db. 

### Available methods

### GET `/movies/{movie_id}`

Retrieves the movie with the specified id. If no id is provided, the entire movies database is returned.  

Sample response body:
```
{
    "id": "e6068a8f-fb38-49b5-a1a9-2e1222a2bdce",
    "title": "Die Hard", 
    "year": 1988
}
```

### POST `/movies/`

Creates a new movie in the database based on the json passed to the call. `title` and `year` are required fields. When successful, the new movie will be included in the response. 

Sample request body:
```
{
    "title": "Die Hard", 
    "year": 1988
}
```

Sample response body:
```
{
    "id": "e6068a8f-fb38-49b5-a1a9-2e1222a2bdce",
    "title": "Die Hard", 
    "year": 1988
}
```

### PUT `/movies/{movie_id}`

Will search the database for an id match and update the movie based on the json passed. In this scenario, any combination of valid movie properties can be updated at a time. If no movie can be found, a new one will be created. If a new movie is created, the request will be rejected if the json body does not include all required properties: `title` and `year`. The new/edited movie will be returned in the response. 

Sample request body:
```
{
    "year": 1600
}
```

Sample response body:
```
{
    "id": "e6068a8f-fb38-49b5-a1a9-2e1222a2bdce",
    "title": "Die Hard", 
    "year": 1600
}
```

### DELETE `/movies/{movie_id}`

Deletes the movie with the specified id. 


## Search

Searches the entire database. 

### Available methods

### GET `/search/{query}`

Returns all database entries with a string field that (partially) matches the query, regardless of case. Multiple query values can be supplied and should be separated by a `-`. 

Sample query: `arnold-true`

Sample response body:
'''
[
    {
        'first_name': 'Arnold', 
        'last_name': 'Schwarzenegger', 
        'id': 'b9f2d28c-57dc-4381-a752-ac36611ab51a', 
        'birth_year': 1947
    }, 
    {
        'year': 1994, 
        'id': '2ed05e37-1659-4213-a82b-eb5e3ded22c8', 
        'title': 'True Lies'
    }
]
```
