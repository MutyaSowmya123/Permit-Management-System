
# Permit Management System

A Flask-based backend system for permit applications where users can register, submit permit applications, and track their status. Admins can approve or reject applications.

## Features

- User registration and authentication with JWT
- Permit application submission and management
- Admin approval/rejection workflow
- RESTful API with validation
- PostgreSQL database with SQLAlchemy ORM
- Docker containerization
- Automated testing with pytest
- CI/CD with GitHub Actions

## Prerequisites

- Docker and Docker Compose
- Git

## Quick Start with Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Permit-Management-System
   ```

2. **Start the application:**
   ```bash
   docker-compose up --build
   ```

   This will:
   - Build the Flask application container
   - Start PostgreSQL database
   - Run database migrations
   - Start the Flask app on http://localhost:5000

3. **Access the application:**
   - API endpoints: http://localhost:5000/api/
   - Home page: http://localhost:5000/

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get JWT token

### Permit Management (User)
- `POST /api/permit/submit` - Submit permit application (requires JWT)
- `GET /api/permit/my-permits` - View user's permits (requires JWT)
- `PUT /api/permit/<id>` - Update permit (requires JWT)
- `DELETE /api/permit/<id>` - Delete permit (requires JWT)

### Admin Functions
- `PUT /api/admin/approve/<id>` - Approve permit (admin only)
- `PUT /api/admin/reject/<id>` - Reject permit (admin only)
- `GET /api/admin/permits` - List all permits (admin only)

## Testing the API

### Register a User
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

Use the returned `access_token` in subsequent requests:

### Submit Permit
```bash
curl -X POST http://localhost:5000/api/permit/submit \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{"description": "Refrigeration permit for new store"}'
```

## Development Setup (Without Docker)

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up PostgreSQL:**
   - Install PostgreSQL locally
   - Create database: `permits`
   - Update `config.py` or set environment variables

3. **Run migrations:**
   ```bash
   flask db upgrade
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```

## Environment Variables

Create a `.env` file in the root directory:

```
DB_URL=postgresql://postgres:Sowmya@123@localhost:5432/permits
JWT_SECRET_KEY=your-secret-key-here
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## CI/CD

The project includes GitHub Actions workflow that:
- Builds and tests the application on every push/PR
- Uses Docker Compose for containerized testing
- Runs automated tests

## Project Structure

```
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # SQLAlchemy models
│   ├── routes/              # API blueprints
│   │   ├── auth.py
│   │   ├── permit.py
│   │   └── admin.py
│   ├── schemas/             # Marshmallow schemas
│   └── templates/           # Jinja2 templates
├── tests/                   # Pytest tests
├── migrations/              # Database migrations
├── .github/workflows/       # CI/CD workflows
├── docker-compose.yml       # Docker services
├── Dockerfile               # Container definition
├── requirements.txt         # Python dependencies
└── run.py                   # Application entry point
```

## Technologies Used

- **Flask**: Web framework
- **SQLAlchemy**: ORM
- **PostgreSQL**: Database
- **JWT**: Authentication
- **Marshmallow**: Data validation/serialization
- **Docker**: Containerization
- **pytest**: Testing
- **GitHub Actions**: CI/CD

