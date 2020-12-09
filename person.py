from flask import (
  make_response,
  abort,
)
from config import db
from models import (
  Person,
  PersonSchema,
)
def read_all():
  """
  This function responds to a request for /api/people
  with the complete lists of people
  :return:    json string of list of people
  """
  # Create the list of people from our data
  people = Person.query \
    .order_by(Person.lname) \
    .all()
  # Serialize the data for the response
  person_schema = PersonSchema(many=True)
  return person_schema.dump(people).data
def read_one(person_id):
  """
  This function responds to a request for /api/people/{person_id}
  with one matching person from people
  :param person_id:  ID of person to find
  :return:      person matching ID
  """
  # Get the person requested
  person = Person.query \
    .filter(Person.person_id == person_id) \
    .one_or_none()
  # Did we find a person?
  if person is not None:
    # Serialize the data for the response
    person_schema = PersonSchema()
    return person_schema.dump(person).data
  # Otherwise, nope, didn't find that person
  else:
    abort(404, 'Person not found for Id: {person_id}'.format(person_id=person_id))

    def create(person):
        """
        This function creates a new person in the people structure
        based on the passed-in person data
        :param person: person to create in people structure
        :return:    201 on success, 406 on person exists
        """
        fname = person.get('fname')
        lname = person.get('lname')
        existing_person = Person.query \
            .filter(Person.fname == fname) \
            .filter(Person.lname == lname) \
            .one_or_none()
        # Can we insert this person?
        if existing_person is None:
            # Create a person instance using the schema and the passed-in person
            schema = PersonSchema()
            new_person = schema.load(person, session=db.session).data
            # Add the person to the database
            db.session.add(new_person)
            db.session.commit()
            # Serialize and return the newly created person in the response
            return schema.dump(new_person).data, 201
        # Otherwise, nope, person exists already
        else:
            abort(409, f'Person {fname} {lname} exists already')