# Nombre Eduardo David Gómez Miranda proyecto sprint 7
# Proyecto Urban Grocers
# Descripción del objetivo:
# El propósito de Urban Grocers es desarrollar un sistema para generar kits con distintos productos para cada usuario que se registre,
# asignando de forma aleatoria un token, el cual guardará los datos del kit correspondiente.
#Tecnologías utilizadas 
Python 3.x
PyTest
APIdocs
# Instrucciones para configurar el entorno
Se usa: git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
# Utilizar la documentación API
La documentación del API se genera utilizando APIdocs. Para visualizarla
# Explicación de como aplicar las pruebas desde tu terminal de computadora
Desde la raíz del proyecto (donde se encuentran tus archivos .py y tus tests):
pytest
Este comando buscará automáticamente todos los archivos que comiencen con test_ o terminen con _test.py y ejecutará sus funciones de prueba.
Comando detallado
Para obtener una salida más descriptiva de las pruebas, puedes usar la opción -v
pytest -v
Para ver los print() dentro de tus pruebas (útil para depuración):
pytest -s
Seguir comandos para enlazar el trabajo con Github
# Para realizar las pruebas en pytest usar el siguiente comando
pytest ruta/del/proyecto
# Instrucciones para realizar las pruebas:
# 1. Consultar las APIs usando las rutas URL_SERVICE, CREATE_USER_PATH y PRODUCT_KITS_PATH del registro de APIs.
# 2. Crear un nuevo perfil de usuario proporcionando los siguientes datos: 
# 3.body_user = { "firstName": "Max", "email": "max@example.com", "phone": "+10005555355", "comment": "test" }.
# 4. Guardar el token generado para el usuario en una variable, con el fin de utilizarlo posteriormente al crear el kit.
# 5. Generar el kit utilizando el token del usuario y almacenar la información del mismo.
# 6. Establecer los posibles resultados esperados, como códigos 201 (éxito) y 400 (error).
# 7. Definir los escenarios de prueba en función de esos valores esperados.
# 8.Ejecutar las pruebas, diferenciando entre casos válidos e inválidos.
# 9. Comprobar que los resultados coincidan con lo que se espera en cada caso.
