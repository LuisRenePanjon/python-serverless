from src.config.db import engine
from src.models.Users import User
from src.models.Addresses import Address
from sqlalchemy.orm import Session


def create_user(event, context):

    with Session(engine) as session:
        spongebob = User(
            name="other user",
            fullname="xd",
            addresses=[Address(email_address="xd@sqlalchemy.org")],
        )
        sandy = User(
            name="sandy new",
            fullname="Sandy Cheeks new",
            addresses=[
                Address(email_address="new_one@sqlalchemy.org"),
                Address(email_address="new_two@squirrelpower.org"),
            ],
        )
        patrick = User(name="patrick", fullname="Patrick Star")
        session.add_all([spongebob, sandy, patrick])
        session.commit()
    return {
        "statusCode": 200,
        "body": "Users created successfully"
    }

