const express = require('express');
const jwt = require('jsonwebtoken');
const sqlite3 = require('sqlite3').verbose();
const { MercadoPagoConfig, Preference } = require('mercadopago'); // Cambia a Preference para simplicidad

// Configura MercadoPago con tu access token (reemplaza con tu token real de sandbox o producción)
const client = new MercadoPagoConfig({
  accessToken: 'APP_USR-3019635509030048-101111-6b777448d02697c001c636158c99ebef-210254714', // Obtén de https://www.mercadopago.com.ar/developers
  options: { timeout: 5000 }
});

const preference = new Preference(client); // Usa Preference en lugar de Order

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

// Endpoint para procesar pago (usando Preference de MercadoPago)
app.post('/create-payment', async (req, res) => {
  const { email } = req.body;
  const body = {
    items: [{
      title: 'Licencia App',
      unit_price: 1000, // Precio en ARS
      quantity: 1,
      currency_id: 'ARS'
    }],
    payer: {
      email: email
    },
    back_urls: {
      success: 'https://httpbin.org/get?status=success', // URL pública dummy para testing
      failure: 'https://httpbin.org/get?status=failure',
      pending: 'https://httpbin.org/get?status=pending'
    }
    // Quita auto_return para evitar validaciones
  };

  try {
    const response = await preference.create({ body });
    res.json({ url: response.init_point }); // URL para pagar
  } catch (error) {
    console.error('Error de MercadoPago:', error.message); // Agrega logging detallado
    res.status(500).json({ error: 'Error al crear el pago', details: error.message });
  }
});

app.listen(3000, () => console.log('Servidor corriendo en puerto 3000'));

// Endpoints para back_urls (simples para testing)
app.get('/success', (req, res) => res.send('Pago exitoso!'));
app.get('/failure', (req, res) => res.send('Pago fallido.'));
app.get('/pending', (req, res) => res.send('Pago pendiente.'));