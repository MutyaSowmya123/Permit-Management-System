import time
from sqlalchemy.exc import OperationalError
from app import create_app, db
from dotenv import load_dotenv

load_dotenv()

app = create_app()

with app.app_context():
    for i in range(10):
        try:
            db.create_all()
            print("Database ready")
            break
        except OperationalError:
            print("Waiting for database...")
            time.sleep(2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
