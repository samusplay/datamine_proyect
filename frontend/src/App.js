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
  const [numeroContador, setNumeroContador] = useState('');
  const [error, setError] = useState('');

  // Función simulada para enviar los datos a la API
  const enviarDatosAPI = () => {
    console.log("Datos enviados a la API:", { nombre, tipoUsuario: selectedTipo, numeroContador });
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

  // Maneja el cambio en el número de contador
  const handleNumeroContadorChange = (event) => {
    const value = event.target.value;
    setNumeroContador(value);
    
    // Validación: el número de contador debe ser un número positivo y de una longitud adecuada
    if (!/^\d+$/.test(value)) {
      setError("El número de contador debe contener solo dígitos.");
    } else if (value.length < 5) {
      setError("El número de contador debe tener al menos 5 dígitos.");
    } else {
      setError('');
    }
  };

  // Manejar el clic en el botón "continuar"
  const handleContinue = () => {
    if (nombre === '' || selectedTipo === '') {
      alert("Por favor, ingresa todos los datos.");
      return;
    }
    
    if (error === '' && numeroContador !== '') {
      enviarDatosAPI();
      alert(`Datos registrados:\nNombre: ${nombre}\nTipo de Usuario: ${selectedTipo}\nNúmero de Contador: ${numeroContador}`);
    } else {
      alert("Por favor, revisa el número de contador.");
    }
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

        {/* Input para ingresar el número de contador */}
        {selectedTipo && nombre && (
          <div className="formulario">
            <label htmlFor="numeroContador">Número de Contador:</label>
            <input 
              type="text" 
              id="numeroContador" 
              value={numeroContador} 
              onChange={handleNumeroContadorChange} 
              placeholder="Escribe el número de contador"
            />
            {error && <p className="error">{error}</p>}
          </div>
        )}

        {/* Botón Continuar */}
        {selectedTipo && nombre && numeroContador && !error && (
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
      </header>
    </div>
  );
}

export default App;

