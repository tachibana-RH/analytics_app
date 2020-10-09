import os
from flask_script import Manager, Server
from app import app

manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = str(os.getenv('HOST', '0.0.0.0')),
    port = str(os.getenv('PORT', '5000'))
    )
)

if __name__ == '__main__':
    manager.run()