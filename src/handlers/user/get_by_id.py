import json
from src.config.db import engine
from src.models.Users import User
from src.models.Addresses import Address
from sqlalchemy.orm import Session
from sqlalchemy import select


def get_user(event, context):
    try:
        with Session(engine) as session:
            user = session.execute(select(User).filter_by(id=event['pathParameters']['id'])).scalar_one()
            # check if user not found
            user_json = {
                "id": user.id,
                "name": user.fullname,
            }
            return {
                "statusCode": 200,
                "body": json.dumps(user_json)
            }
    except:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": f"User not found"})
        }
