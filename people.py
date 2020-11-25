
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = [
  {
    "fname": "Kent",
    "lname": "Brockman",
    "timestamp": "2018-05-10 18:12:42"
  },
  {
    "fname": "Bunny",
    "lname": "Easter",
    "timestamp": "2018-05-10 18:12:42"
  },
  {
    "fname": "Doug",
    "lname": "Farrell",
    "timestamp": "2018-05-10 18:12:42"
  }
]


def read():


    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]