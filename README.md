# Contact List Manager Application

A simple full-stack contact manager application built with **React** on the frontend and **Express + SQLite** on the backend. This app allows users to **add**, **view**, **search**, and **delete** contacts in a clean and responsive UI.

---

##  How to Run the App

### Prerequisites

- Node.js (v18 or later recommended)
- npm (comes with Node)
- SQLite3

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/contact-list-manager.git
cd contact-list-manager
````

---

### 2. Install Server Dependencies

```bash
cd server
npm install
```

---

### 3. Start the Backend Server

```bash
node server.js
```

* Runs at: `http://localhost:3001`
* `contacts.db` is created automatically

---

### 4. Install Client Dependencies

Open a **second terminal**:

```bash
cd client
npm install
```

---

### 5. Start the Frontend (React)

```bash
npm start
```

* Runs at: `http://localhost:3000`

---

## Features

*  Add a new contact (name + email)
*  Search contacts by name or email
*  Delete a contact
*  Styled with responsive, clean design
*  Basic frontend tests with React Testing Library

---

## Running Tests

### Client (React) Tests

```bash
cd client
npm test
```

* Uses `@testing-library/react` and `@testing-library/jest-dom`

---

## Technologies Used

### Frontend

* React
* Axios
* React Testing Library
* Plain CSS

### Backend

* Express.js
* SQLite3
* Node.js

---

##  Trade-offs & Design Decisions

* **SQLite** was chosen for simplicity (lightweight, file-based), ideal for a small app. For production, PostgreSQL or MongoDB would be better.
* **No authentication** to keep scope small in real-world apps, user auth is essential.
* **Minimal UI styling** was used instead of a UI framework like Tailwind or Material UI to keep the app lightweight.
* **Basic validation only** assumes valid email input; could be enhanced later.

---

##  Future Improvements

*  Add user authentication and protected routes
*  Validate and sanitize email input
*  Improve mobile responsiveness and accessibility
*  Add loading states and error UI
*  Expand backend tests with Supertest

---

## 👤 Author

Made with ❤️ by **Sowmya Mutya**.

Feel free to contribute, fork, or reach out!

---
