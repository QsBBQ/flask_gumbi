from gumbi.db.database import db_session as s, init_db
from gumbi.db.models import User, Widget, Planet
from faker import Factory
# init_db()

# u = User('Bob', 'bob@bob.com')
#
# s.add(u)
# s.commit()


# user_query = User.query.all()
# for user in user_query:
#     print(user.name, user.email)
fake = Factory.create()
for _ in range(0,1000):
    user = User(fake.name(), fake.email())
    s.add(user)
    s.commit()
