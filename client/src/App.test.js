import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';

jest.mock('axios', () => ({
  get: jest.fn(),
  post: jest.fn(),
  delete: jest.fn(),
}));

import axios from 'axios';


test('renders contact list manager and adds contact', async () => {
  axios.get.mockResolvedValue({ data: [] });
  axios.post.mockResolvedValue({});
  axios.get.mockResolvedValueOnce({ data: [] }).mockResolvedValueOnce({ data: [{ id: 1, name: 'John', email: 'john@example.com' }] });

  render(<App />);

  expect(screen.getByText(/Contact List Manager/i)).toBeInTheDocument();

  fireEvent.change(screen.getByPlaceholderText(/Name/i), { target: { value: 'John' } });
  fireEvent.change(screen.getByPlaceholderText(/Email/i), { target: { value: 'john@example.com' } });

  fireEvent.click(screen.getByText(/Add Contact/i));

  await waitFor(() => {
    expect(screen.getByText(/John/i)).toBeInTheDocument();
  });
});
