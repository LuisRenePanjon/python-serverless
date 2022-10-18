import json
from src.config.db import engine
from src.models.Users import User
from src.models.Addresses import Address
from sqlalchemy.orm import Session
from sqlalchemy import select


def get_users(event, context):
    with Session(engine) as session:
        users = session.execute(select(User)).scalars().all()
        users_to_response = []
        for user in users:
            user_json = {
                "id": user.id,
                "name": user.fullname,
            }
            users_to_response.append(user_json)

        return {
            "statusCode": 200,
            "body": json.dumps(users_to_response)
        }
