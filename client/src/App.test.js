// src/App.test.js
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';

jest.mock('./api/contacts', () => ({
  fetchContacts: jest.fn(),
  addContact: jest.fn(),
  deleteContact: jest.fn(),
}));

import { fetchContacts, addContact, deleteContact } from './api/contacts';

test('renders and adds contact', async () => {
  fetchContacts.mockResolvedValueOnce({ data: [] });
  addContact.mockResolvedValueOnce({});
  fetchContacts.mockResolvedValueOnce({ data: [{ id: 1, name: 'John', email: 'john@example.com' }] });

  render(<App />);

  expect(screen.getByText(/Contact List Manager/i)).toBeInTheDocument();

  fireEvent.change(screen.getByPlaceholderText(/Name/i), { target: { value: 'John' } });
  fireEvent.change(screen.getByPlaceholderText(/Email/i), { target: { value: 'john@example.com' } });
  fireEvent.click(screen.getByText(/Add Contact/i));

  await waitFor(() => {
    expect(screen.getByText(/john@example.com/i)).toBeInTheDocument();
  });
});
