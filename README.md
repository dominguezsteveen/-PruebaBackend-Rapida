# -PruebaBackend-Rapida
Este es un proyecto desarrollado en el framework Flask de python, con el objetivo de presentar la prueba tecnica de Talento Humano. Tiene como funcionalidad el consumo de recurso REST API que busca una subcadena que sea palindromo.

# Inicio
- Se debe tener python instalado en el computador
- Se clona el proyecto con git clone, o descargarlo.
- Por medio del cmd nos movemos a la carpeta del proyecto
- Ejecutamos pip install flask para instalar las dependencias de flask
- Corremos el comando python app.py para iniciar el servidor.

# Estructura json
  La estructura que debe tener como minimo el json que se le manda al endpoint /palindromo por el metodo POST debe ser la siguiente:
    {
      "user"="admin",
      "password"="4DM!N",
      "cadena"="cadena que se desee"
    }
# Logica
El aplicativo valida el usuario y contraseña que se le está dando en el json y si todo está correcto, valida la cadena ingreseda y busca la subcadena que sea más larga. Si encuentra algún error o incongruencia devuelve un mensaje de error.
