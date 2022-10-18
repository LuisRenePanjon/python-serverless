import json
from requests import get


def hello(event, context):
    pokemon = get('https://pokeapi.co/api/v2/pokemon/ditto')
    pokemon_name = pokemon.json()['name']
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    # create a response with all pokemon info
    response = {
        "statusCode": 200,
        "body": json.dumps(pokemon.json())
    }

    return response
