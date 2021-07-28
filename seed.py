from app import db
from app.models import Menu

class Seeder(object):
    def populate_database(self):
        record = Menu.query.first()
        if not record:
            new_record = Menu(name="Baked potatoes",price="10",quantity="500gm")
            db.session.add(new_record)

            new_record = Menu(name="Garlic bread",price="50",quantity="2pcs")
            db.session.add(new_record)
            new_record = Menu(name="Fried rice",price="100",quantity="500gm")
            db.session.add(new_record)
            new_record = Menu(name="Soup",price="30",quantity="500gm")
            db.session.add(new_record)

            db.session.commit()

if __name__ == '__main__':
    print("Seeding...")
    seeder = Seeder()
    seeder.populate_database()
    print("Seeding complete.")
