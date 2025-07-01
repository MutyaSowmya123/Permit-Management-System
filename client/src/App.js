import { useEffect, useState } from "react";
import axios from "axios";
import './App.css';

const API = "http://localhost:3001/contacts";

function App() {
  const [contacts, setContacts] = useState([]);
  const [form, setForm] = useState({ name: "", email: "" });
  const [search, setSearch] = useState("");

  const fetchContacts = async (searchText = "") => {
    const res = await axios.get(API, {
      params: { search: searchText },
    });
    setContacts(res.data);
  };

  useEffect(() => {
    fetchContacts();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(API, form);
      setForm({ name: "", email: "" });
      fetchContacts();
    } catch (err) {
      alert(err.response?.data?.error || "Error");
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this contact?"))
      return;

    try {
      await axios.delete(`${API}/${id}`);
      fetchContacts(search);
    } catch (err) {
      alert(err.response?.data?.error || "Delete failed");
    }
  };

  return (
    <div className="container">
      <h1>Contact List Manager</h1>

      <form onSubmit={handleSubmit}>
        <input
          placeholder="Name"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
          required
        />
        <input
          placeholder="Email"
          type="email"
          value={form.email}
          onChange={(e) => setForm({ ...form, email: e.target.value })}
          required
        />
        <button type="submit">Add Contact</button>
      </form>

      <input
        placeholder="Search"
        value={search}
        onChange={(e) => {
          setSearch(e.target.value);
          fetchContacts(e.target.value);
        }}
      />

      <ul className="contact-list">
        {contacts.map((c) => (
          <li key={c.id} className="contact-item">
            <span>
              {c.name} ({c.email})
            </span>
            <button
              onClick={() => handleDelete(c.id)}
              className="delete-button"
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
