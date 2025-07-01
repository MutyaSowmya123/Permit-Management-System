import React from 'react';

const ContactList = ({ contacts, onDelete }) => (
  <ul className="contact-list">
    {contacts.map((c) => (
      <li key={c.id} className="contact-item">
        <span>{c.name} ({c.email})</span>
        <button className="delete-button" onClick={() => onDelete(c.id)}>Delete</button>
      </li>
    ))}
  </ul>
);

export default ContactList;
