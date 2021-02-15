import os
import sys
import flask_script
from application import create_app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = create_app()
manager = flask_script.Manager(app)

# turn on debugger by default and reloader
manager.add_command("runserver", flask_script.Server(use_debugger=True, use_reloader=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080))))

if __name__ == "__main__":
    manager.run()
