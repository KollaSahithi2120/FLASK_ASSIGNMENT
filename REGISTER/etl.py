from app import create_app, db
from app.models import Role

def create_roles():
    roles = ['Admin', 'Editor', 'Viewer']
    for role_name in roles:
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            new_role = Role(name=role_name)
            db.session.add(new_role)
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        create_roles()
        print('ETL process completed.')
