from gumbi.db.database import db_session as s, init_db
from gumbi.db.models import User, Widget, Planet
# from ..db.database import db_session as s, init_db
# from ..db.models import User, Widget, Planet

class MyTest:
    def __init__(self):
        pass
    def load_user(self):
        u = User('Cory', 'corey@bob.com')

        s.add(u)
        s.commit()
    def show_users(self):
        user_query = User.query.all()
        for user in user_query:
            print(user.name, user.email)
    def show_test(self):
        print("Showing test!")
