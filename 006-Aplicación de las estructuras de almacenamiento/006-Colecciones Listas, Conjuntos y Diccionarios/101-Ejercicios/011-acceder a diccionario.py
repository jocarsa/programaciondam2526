persona = {
	"nombre":"Jose Vicente",
  "apellidos":"Carratalá Sanchis",
  "correo":"info@jocarsa.com",
  "edad":47,
  "telefonos":[
  	{	
      "tipo":"fijo",
    	"número":96123455
    },
    {	
      "tipo":"movil",
    	"número":65456546
    }
  ]
}

print(persona)
print(persona["telefonos"][0]["número"])