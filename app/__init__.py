from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.settings import Config

    
# Create a Flask app
app = Flask(__name__)
config = Config()

app.config.from_object(config)


# Run the Flask app
if __name__ == '__main__':
    app.run()
