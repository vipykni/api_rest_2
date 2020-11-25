from datetime import datetime

from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Mazolina": {
        "fname": "Dazdraperma",
        "lname": "Mazolina",
        "timestamp": get_timestamp(),
    },
    "Makienka": {
        "fname": "Maksim",
        "lname": "Makienka",
        "timestamp": get_timestamp(),
    },
    "Makienko": {
        "fname": "Aleksander",
        "lname": "Makienko",
        "timestamp": get_timestamp(),
    },
}



def read_all():

    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(lname):

    if lname in PEOPLE:
        person = PEOPLE.get(lname)


    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

    return person


def create(person):

    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201


    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )


def update(lname, person):

    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]


    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )


def delete(lname):

    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )


    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )