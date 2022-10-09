#!/usr/bin/python3
""" lists all State objects from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_city import City


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

#     states_with_cities = session.query(State).join(City, State.id).order_by(cities.id)
#     print(states_with_cities)

#     for c, i in session.query(Customer, Invoice).filter(Customer.id == Invoice.custid).all():
#    print ("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id,c.name, i.invno, i.amount))

    for city, state in session.query(City, State).filter(City.state_id == State.id).order_by(City.id):
       print("{}: ({}) {}".format(state.name, city.id, city.name))
