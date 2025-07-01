import express from 'express';
import cors from 'cors';
import { dbPromise, initDB } from './db.js';

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());

await initDB();

app.get('/contacts', async (req, res) => {
  const db = await dbPromise;
  const { search } = req.query;
  let contacts;

  if (search) {
    contacts = await db.all(
      `SELECT * FROM contacts WHERE name LIKE ? OR email LIKE ?`,
      [`%${search}%`, `%${search}%`]
    );
  } else {
    contacts = await db.all(`SELECT * FROM contacts`);
  }

  res.json(contacts);
});

app.post('/contacts', async (req, res) => {
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

app.delete('/contacts/:id', async (req, res) => {
  const db = await dbPromise;
  const id = req.params.id;
  try {
    const result = await db.run('DELETE FROM contacts WHERE id = ?', id);
    if (result.changes === 0) {
      return res.status(404).json({ error: 'Contact not found' });
    }
    res.json({ message: 'Contact deleted' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});


app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
