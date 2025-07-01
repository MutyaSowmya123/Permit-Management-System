import express from 'express';
import cors from 'cors';
import { initDB } from './db.js';
import contactRoutes from './routes/contacts.js';

const app = express();
const PORT = 3001;

await initDB();

app.use(cors());
app.use(express.json());
app.use('/contacts', contactRoutes);

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
