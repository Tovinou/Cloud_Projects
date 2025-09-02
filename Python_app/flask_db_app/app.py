from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@db:5432/mydb"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route("/")
def index():
    users = User.query.all()
    return "<br>".join([u.name for u in users]) or "Inga användare i databasen"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
