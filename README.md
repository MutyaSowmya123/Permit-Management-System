
# Contact List Manager

A full-stack web application to manage a list of contacts using a simple and modern UI. This project allows users to **add**, **search**, and **delete** contacts. The application is built using **React** for the frontend and **Node.js/Express** with **SQLite** for the backend.

The project follows a modular folder structure, separating concerns such as components, API calls, and styles, making the codebase clean and maintainable.

---

## Tech Stack

### Frontend
- React (Functional Components + Hooks)
- Axios for HTTP requests
- CSS for styling
- React Testing Library & Jest for testing

### Backend
- Node.js + Express.js
- SQLite (via `sqlite3` and `sqlite` npm packages)
- RESTful API with structured routing

---

## Features

-  Add a new contact with name and email
-  Search contacts by name or email
-  Delete existing contacts
-  Responsive and modular UI components
-  Unit testing setup for frontend functionality
-  Concurrent dev server setup to run both frontend and backend simultaneously

---

## Project Structure

```

contact-list-manager/
├── client/                   # React frontend
│   ├── public/
│   ├── src/
│   │   ├── api/              # Axios API layer
│   │   ├── components/       # ContactForm, ContactList, SearchBar
│   │   ├── styles/           # App.css
│   │   ├── App.js
│   │   ├── App.test.js
│   │   └── index.js
│   └── package.json
│
├── server/                   # Express backend
│   ├── routes/               # contacts.js route
│   ├── db.js                 # DB init and connection
│   ├── server.js             # Express setup and server
│   └── package.json
│
├── package.json              # Root-level scripts to run both client and server
└── README.md                 # Project documentation

````

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/contact-list-manager.git
cd contact-list-manager
````

### 2. Install Dependencies

#### Backend:

```bash
cd server
npm install
```

#### Frontend:

```bash
cd ../client
npm install
```

#### Root:

```bash
cd ..
npm install   # for concurrently
```

### 3. Start the Application

Run both client and server together from root:

```bash
npm start
```

* Frontend available at: `http://localhost:3000`
* Backend API available at: `http://localhost:3001/contacts`

> This setup uses `concurrently` to run both React and Express servers in parallel.

---

## Running Tests

To run the frontend test suite:

```bash
cd client
npm test
```

* The tests cover basic UI rendering and interaction logic.
* API calls are mocked via the modular `api/contacts.js` file.

---

## Design Decisions & Trade-offs

* **SQLite was chosen** for simplicity and quick setup. Since it's a file-based DB, it requires no additional installation or configuration. This is ideal for small-scale applications and take-home projects.

* **No authentication** was implemented to keep the scope focused on contact CRUD functionality. In a production app, you would likely want user accounts and protected endpoints.

* **Custom CSS was used** instead of external UI libraries like Tailwind or Material UI. This gives full control over layout and design while keeping dependencies minimal.

* **The project was modularized** to improve code readability and separation of concerns. API logic, components, and styles are placed in their own folders.

* **The backend does not use any middleware like CORS or proxying** because the frontend uses full URLs (e.g., `http://localhost:3001/contacts`) to access the backend. This avoids proxy configuration but hardcodes the port for local development.

* **Environment variables (`.env`) were not used** since all backend URLs are currently handled directly via constants in the API layer. In a production setup, using environment variables would make this more flexible.

---

## Future Improvements

*  Add Edit/Update functionality for contacts
*  Improve mobile responsiveness and accessibility
*  Add user authentication with JWT/session support
*  Add better client-side and server-side input validation
*  Add loading indicators and error UI states

---

## License

This project is licensed under the **MIT License**.

---

## Author

Made with ❤️ by **Your Name**
[GitHub](https://github.com/your-username)

