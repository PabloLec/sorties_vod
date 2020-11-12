import logging, os, platform
from logging.handlers import RotatingFileHandler

# SCRIPT #

from scripts.grab_movie_list import grab_movie_list

# IMPORT MODULES FLASK #

from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/whatsnew')

### INDEX ###

@app.route("/")
def index():
    movie_list = grab_movie_list()
    return render_template('index.html', title='Nouveautés', name_list=movie_list[0], scrap=movie_list[1])

### ERROR HANDLER ###

@app.errorhandler(500)
def internal_error(exception):
    app.logger.error(exception)
    return render_template('500.html', exception=exception), 500

if __name__ == "__main__":
    handler = RotatingFileHandler(os.path.dirname(os.path.realpath(__file__))+'/log/flask.log', maxBytes=1000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(ssl_context='adhoc')

print(os.path.dirname(os.path.realpath(__file__)))


