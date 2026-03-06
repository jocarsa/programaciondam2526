const http = require('http');
const servidor = http.createServer((peticion, respuesta) => {
  respuesta.writeHead(200, { 'Content-Type': 'text/plain' });
  respuesta.end('Hola mundo desde node\n');
});
servidor.listen(3001, () => {
  console.log(`Server running at http://localhost:3001/`);
});