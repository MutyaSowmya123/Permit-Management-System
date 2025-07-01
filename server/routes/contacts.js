import express from 'express';
import { dbPromise } from '../db.js';

const router = express.Router();

router.get('/', async (req, res) => {
  const db = await dbPromise;
  const { search } = req.query;
  const query = search
    ? `SELECT * FROM contacts WHERE name LIKE ? OR email LIKE ?`
    : `SELECT * FROM contacts`;
  const params = search ? [`%${search}%`, `%${search}%`] : [];
  const contacts = await db.all(query, params);
  res.json(contacts);
});

router.post('/', async (req, res) => {
  const db = await dbPromise;
  const { name, email } = req.body;

  if (!name || !email) return res.status(400).json({ error: 'Name and email required' });

  try {
    await db.run(`INSERT INTO contacts (name, email) VALUES (?, ?)`, [name, email]);
    res.status(201).json({ message: 'Contact added' });
  } catch (err) {
    if (err.code === 'SQLITE_CONSTRAINT') {
      res.status(409).json({ error: 'Email already exists' });
    } else {
      res.status(500).json({ error: 'Server error' });
    }
  }
});

router.delete('/:id', async (req, res) => {
  const db = await dbPromise;
  const id = req.params.id;
  try {
    const result = await db.run(`DELETE FROM contacts WHERE id = ?`, id);
    if (result.changes === 0) return res.status(404).json({ error: 'Contact not found' });
    res.json({ message: 'Contact deleted' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

export default router;
