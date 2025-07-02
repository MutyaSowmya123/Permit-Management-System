import React from 'react';

const ContactForm = ({ form, setForm, onSubmit }) => (
  <form onSubmit={onSubmit}>
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
);

export default ContactForm;
