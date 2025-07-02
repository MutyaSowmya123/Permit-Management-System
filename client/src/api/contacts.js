import axios from 'axios';

const API_URL = 'http://localhost:3001/contacts';

export const fetchContacts = (search = '') =>
  axios.get(API_URL, { params: { search } });

export const addContact = (form) =>
  axios.post(API_URL, form);

export const deleteContact = (id) =>
  axios.delete(`${API_URL}/${id}`);
