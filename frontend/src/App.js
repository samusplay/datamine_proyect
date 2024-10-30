import React, { useState } from 'react';
import './App.css';
import Usuario from './components/usuario';
import luz_icono from './luz_icono.png';



function App() {
  const [usuarios, setUsuarios] = useState([
    { id: 1, nombre: '', tipoUsuario: 'Inquilino' },
    { id: 2, nombre: '', tipoUsuario: 'Dueño' },
  ]);

  const [selectedTipo, setSelectedTipo] = useState('');
  const [nombre, setNombre] = useState('');

  // Función simulada para enviar los datos a la API
  const enviarDatosAPI = () => {
    console.log("Datos enviados a la API:");
    console.log({ nombre, tipoUsuario: selectedTipo });

    // Código comentado para realizar el POST a la API
    /*
    fetch('URL_DE_LA_API', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        nombre: nombre,
        tipoUsuario: selectedTipo
      })
    }).then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
    */
  };

  // Maneja la selección del tipo de usuario
  const handleTipoChange = (event) => {
    setSelectedTipo(event.target.value);
  };

  // Maneja el cambio en el nombre del usuario
  const handleNombreChange = (event) => {
    setNombre(event.target.value);
    setUsuarios(usuarios.map(user => 
      user.tipoUsuario === selectedTipo ? { ...user, nombre: event.target.value } : user
    ));
  };

  // Manejar el clic en el botón "continuar"
  const handleContinue = () => {
    enviarDatosAPI();  // Llamar a la función que simula el envío de datos a la API
    alert(`Nombre: ${nombre}, Tipo de Usuario: ${selectedTipo}`);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Gestión de Usuarios</h1>

        {/* Nombre de la empresa */}
        <h2 className="nombre-empresa">LuzClick Electric Energy</h2>

        {/* Selección de tipo de usuario */}
        <div className="formulario">
          <label htmlFor="tipoUsuario">Selecciona el tipo de usuario:</label>
          <select id="tipoUsuario" value={selectedTipo} onChange={handleTipoChange}>
            <option value="">-- Selecciona --</option>
            <option value="Inquilino">Inquilino</option>
            <option value="Dueño">Dueño</option>
          </select>
        </div>

        {/* Input para ingresar el nombre */}
        {selectedTipo && (
          <div className="formulario">
            <label htmlFor="nombreUsuario">Escribe tu nombre:</label>
            <input 
              type="text" 
              id="nombreUsuario" 
              value={nombre} 
              onChange={handleNombreChange} 
              placeholder="Escribe tu nombre"
            />
          </div>
        )}

        {/* Botón Continuar */}
        {selectedTipo && nombre && (
          <button className="continuar-btn" onClick={handleContinue}>
            Continuar
          </button>
        )}

        {/* Mostrar los usuarios filtrados por el tipo seleccionado */}
        <div className="usuarios-lista">
          {usuarios
            .filter((user) => selectedTipo === '' || user.tipoUsuario === selectedTipo)
            .map((user) => (
              <Usuario key={user.id} nombre={user.nombre} tipoUsuario={user.tipoUsuario} />
            ))}
        </div>

        <img src={luz_icono} className="App-logo" alt="logo" />
        <p></p>
        <a
        className="App-link"
        href="https://reactjs.org"
        target="_blank"
        rel="noopener noreferrer"
        >
  
</a>

      
      </header>
    </div>
  );
}

export default App;
