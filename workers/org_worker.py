from organizations import Organizations
from db import *


def add_org(name, phone, city, state, active):
    new_org = Organizations(name, phone, city, state, active)

    db.session.add(new_org)
    db.session.commit()


def get_all_active_orgs():
    orgs = db.session.query(Organizations).filter(Organizations.active == True).all()
    orgs_list = []

    for org in orgs:
        current_org = {
            "org_id": org.org_id,
            "name": org.name,
            "phone": org.phone,
            "city": org.city,
            "state": org.state,
            "active": org.active,
        }

        orgs_list.append(current_org)
    return orgs_list


def get_org_by_id(org_id):
    result = (
        db.session.query(Organizations).filter(Organizations.org_id == org_id).one()
    )
    if result:
        user = {
            "org_id": result.org_id,
            "name": result.name,
            "phone": result.phone,
            "city": result.city,
            "state": result.state,
            "active": result.active,
        }
    return user


def update_org(org_dict):
    selected_org = (
        db.session.query(Organizations)
        .filter(Organizations.org_id == org_dict["user_id"])
        .first()
    )

    if selected_org:

        selected_org.name = org_dict["name"]
        selected_org.phone = org_dict["phone"]
        selected_org.city = org_dict["city"]
        selected_org.state = org_dict["state"]
        selected_org.active = org_dict["active"]

        db.session.commit()
    else:
        return "Invalid"


def deactivate_org(org_id):
    selected_org = (
        db.session.query(Organizations).filter(Organizations.org_id == org_id).first()
    )

    if selected_org:
        selected_org.active = False

        db.session.commit()
    else:
        return "Invalid"


def activate_org(org_id):
    selected_org = (
        db.session.query(Organizations).filter(Organizations.org_id == org_id).first()
    )

    if selected_org:
        selected_org.active = True

        db.session.commit()
    else:
        return "Invalid"


def delete_org(org_id):
    selected_org = (
        db.session.query(Organizations).filter(Organizations.org_id == org_id).first()
    )

    db.session.delete(selected_org)
    db.session.commit()
