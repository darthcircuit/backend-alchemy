from db import *
from users import Users


def add_user(first_name, last_name, email, phone, city, state, org_id, active):
    new_user = Users(first_name, last_name, email, phone, city, state, org_id, active)
    db.session.add(new_user)
    db.session.commit()


def get_all_active_users():
    users = db.session.query(Users).filter(Users.active == True).all()
    users_list = []

    for user in users:
        new_user = {
            "user_id": user.user_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "city": user.city,
            "state": user.state,
            "organization": {
                "org_id": user.organization.org_id,
                "name": user.organization.name,
                "phone": user.organization.phone,
                "city": user.organization.city,
                "state": user.organization.state,
            },
            "active": user.active,
        }

        users_list.append(new_user)
    return users_list


def get_user_by_id(user_id):
    result = db.session.query(Users).filter(Users.user_id == user_id).one()
    if result:
        user = {
            "user_id": result.user_id,
            "first_name": result.first_name,
            "last_name": result.last_name,
            "email": result.email,
            "phone": result.phone,
            "city": result.city,
            "state": result.state,
            "org_id": result.org_id,
            "active": result.active,
        }
    return user


def update_user(user_dict):

    selected_user = (
        db.session.query(Users).filter(Users.user_id == user_dict["user_id"]).first()
    )

    if selected_user:

        selected_user.first_name = user_dict["first_name"]
        selected_user.last_name = user_dict["last_name"]
        selected_user.phone = user_dict["phone"]
        selected_user.email = user_dict["email"]
        selected_user.city = user_dict["city"]
        selected_user.state = user_dict["state"]
        selected_user.active = user_dict["active"]
        selected_user.org_id = user_dict["org_id"]

        db.session.commit()
    else:
        return "Invalid"


def deactivate_user(user_id):
    selected_user = db.session.query(Users).filter(Users.user_id == user_id).first()

    if selected_user:
        selected_user.active = False

        db.session.commit()
    else:
        return "Invalid"


def activate_user(user_id):
    selected_user = db.session.query(Users).filter(Users.user_id == user_id).first()

    if selected_user:
        selected_user.active = True

        db.session.commit()
    else:
        return "Invalid"


def delete_user(user_id):
    selected_user = db.session.query(Users).filter(Users.user_id == user_id).first()

    db.session.delete(selected_user)
    db.session.commit()
