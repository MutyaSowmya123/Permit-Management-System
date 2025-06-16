from app import create_app, db
from dotenv import load_dotenv
load_dotenv()


app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
