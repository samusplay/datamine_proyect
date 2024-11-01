// src/api/api.js
import axios from 'axios';



const api = axios.create({
  baseURL: 'http://localhost:8000/api/',  // Cambia localhost:8000 si es necesario en producción
  headers: {
    'Content-Type': 'application/json',
  },
});




export default api;

// src/api/userService.js


export const fetchUsers = async () => {
  try {
    const response = await api.get('/usuarios/');
    return response.data;
  } catch (error) {
    console.error('Error al obtener usuarios:', error);
    throw error;
  }
};
