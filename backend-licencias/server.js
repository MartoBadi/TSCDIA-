const express = require('express');
const jwt = require('jsonwebtoken');
const sqlite3 = require('sqlite3').verbose();
const stripe = require('stripe')('tu_clave_secreta_de_stripe'); // Obtén de Stripe Dashboard

const app = express();
app.use(express.json());

// Base de datos simple
const db = new sqlite3.Database('./licencias.db');
db.run('CREATE TABLE IF NOT EXISTS licencias (id INTEGER PRIMARY KEY, email TEXT, clave TEXT, valida INTEGER)');

// Endpoint para validar licencia
app.post('/validate-license', (req, res) => {
  const { clave } = req.body;
  db.get('SELECT * FROM licencias WHERE clave = ? AND valida = 1', [clave], (err, row) => {
    if (row) {
      const token = jwt.sign({ user: row.email }, 'tu_secreto_jwt'); // Cambia 'tu_secreto_jwt'
      res.json({ valid: true, token });
    } else {
      res.json({ valid: false });
    }
  });
});

// Endpoint para procesar pago (simplificado)
app.post('/create-payment', async (req, res) => {
  const { email } = req.body;
  // Integra con Stripe para crear sesión de pago
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    line_items: [{ price_data: { currency: 'usd', product_data: { name: 'Licencia App' }, unit_amount: 1000 }, quantity: 1 }],
    mode: 'payment',
    success_url: 'http://tu-servidor/success?email=' + email,
  });
  res.json({ url: session.url });
});

app.listen(3000, () => console.log('Servidor corriendo en puerto 3000'));