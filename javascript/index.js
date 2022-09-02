// require to pass the express module; having built-in body-parser middleware, 
// set up app and port variables

const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

const db = require('./queries');

app.use(bodyParser.json());
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
);

// GET request

app.get ('/', (request, response) => {
  response.json({ info: 'Node.js, Express, and Postgres API' });
});

app.get('/users', db.getUsers);
app.get('/users/:id', db.getUsersById);
app.post('/users', db.createUser);
app.put('/users/:id', db.updateUser);
app.delete('/users/:id', db.deleteUser);

// Setting up app to listen on the port 

app.listen(port, () => {
  console.log(`App running on port ${port}.`);
});


