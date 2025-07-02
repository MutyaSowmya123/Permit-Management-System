import { useEffect, useState } from 'react';
import './styles/App.css';
import ContactList from './components/ContactList';
import ContactForm from './components/ContactForm';
import SearchBar from './components/SearchBar';
import { fetchContacts, addContact, deleteContact } from './api/contacts';

function App() {
  const [contacts, setContacts] = useState([]);
  const [form, setForm] = useState({ name: '', email: '' });
  const [search, setSearch] = useState('');

  const loadContacts = async (searchText = '') => {
    const res = await fetchContacts(searchText);
    setContacts(res.data);
  };

  useEffect(() => {
    loadContacts();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addContact(form);
      setForm({ name: '', email: '' });
      loadContacts();
    } catch (err) {
      alert(err.response?.data?.error || 'Error');
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this contact?')) return;
    try {
      await deleteContact(id);
      loadContacts(search);
    } catch (err) {
      alert(err.response?.data?.error || 'Delete failed');
    }
  };

  return (
    <div className="container">
      <h1>Contact List Manager</h1>
      <ContactForm form={form} setForm={setForm} onSubmit={handleSubmit} />
      <SearchBar search={search} setSearch={setSearch} onSearch={loadContacts} />
      <ContactList contacts={contacts} onDelete={handleDelete} />
    </div>
  );
}

export default App;
