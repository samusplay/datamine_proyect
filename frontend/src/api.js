// frontend/src/api.js

import axios from 'axios';

// Configuracion de Axios con la url  base de la Api

const API=axios.create(
    {
        baseUrl:'http://127.0.0.1:8000/api/'//replazar si se va usar otra Api

    }
);
export default API;