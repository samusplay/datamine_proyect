import React, { useState } from 'react';
import './App.css';
import logo from './logo.svg';

function App() {
  const [usuarios] = useState([
    { id: 1, nombre: 'Alejandro', tipoUsuario: 'Inquilino' },
    { id: 2, nombre: 'Johan', tipoUsuario: 'Dueño' },
  ]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Gestión de Usuarios</h1>

        {/* Renderizamos la lista de usuarios */}
        <div className="usuarios-lista">
          {usuarios.map((user) => (
            <div key={user.id} className="usuario-card">
              <h2>{user.nombre}</h2>
              <p>Tipo de Usuario: {user.tipoUsuario}</p>
            </div>
          ))}
        </div>

        {/* Logo y contenido adicional */}
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edita el archivo <code>src/App.js</code> y guarda para recargar.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Aprende React
        </a>
      </header>
    </div>
  );
}

export default App;

