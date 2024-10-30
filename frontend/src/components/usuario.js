import React from "react";

const Usuario = ({ nombre, tipoUsuario }) => {
    if (!nombre) return null;  // Si el nombre está vacío, no mostramos nada.
    return (
      <div className="usuario">
        <h2>{nombre}</h2>
        <p>Tipo de Usuario: {tipoUsuario}</p>
      </div>
    );
  };
  
  export default Usuario;