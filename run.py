from flask import Flask
from app.api import views
app = Flask(__name__)


if __name__ == '__main__':
    app.run()