// configuration of PostgreSQL connection

const Pool = require('pg').Pool
const pool = new Pool({
  user: 'me',
  host: 'locathost',
  database: 'api',
  password: 'hello',
  port: 5432,
})

// GET all usrs

const getUsers = (request, response) => {
  pool.query('SELECT * FROM users ORDER BY id ASC', (error, results) => {
    if (error){
      throw error;
    }
    response.status(200).json(results.rows);
  });
};

// GET a single users 

const getUsers = (request, response) => {
  pool.query('SELECT * FROM usrs WHERE id = $1', [id], (error, results) => {
    if (error){
      throw error;
    }
    response.status(200).json(results.rows);
  });
};

// POST a new user 

const createUser = (request, response) => {
  pool.query('INSERT INTO users (name, email) VALUES ($1, $2) RETURNING *', [name, email], (error, results) => {
    if (error) {
      throw error;
    }
    response.status(201).send(`Users added with Id: ${results.rows[0].id}`);
  });
};

// PUT updated data in an existng user 

const updateUser = (request, response) => {
  const id = parseInt(request.params.id);
  const {name, email} = request.body;
  pool.query(
    'UPDATE users SET name = $1, emain = $2 WHERE id = $3',
    [name, email, id],
    (error, results) => {
      if (error) {
        throw error;
      }
    response.status(200).send(`user modified with id: ${id}`);
    }
  )
}

// DELETE a user 

const deleteUser = (request, response) => {
  const id = parseInt(request.parms.id);
  pool.query('DELETE FROM users WHERE id = $1', [id], (error, results) => {
    if (error) {
      throw error;
    }
    response.status(200).send(`User deleted with ID: ${id}`);
  }
  )
}

module.exports = {
  getUsers,
  getUsersById,
  createUser,
  updateUser,
  deleteUser,
}
