from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell, Manager
from myblog.app import create_app,db
from myblog.app.models import Post,User

app = create_app(config_name='default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(
        app=app, db=db, Post=Post, User=User
    )


manager.add_command('shell', Shell(make_shell_context()))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
