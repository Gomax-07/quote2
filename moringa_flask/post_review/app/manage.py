from app import app
from app import create_app,db
from app import manager
from app import User

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )


if __name__ == '__main__':
    manager.run()