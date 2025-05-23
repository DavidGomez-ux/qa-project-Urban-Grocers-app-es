# Proyecto Urban Grocers
# Descripción del objetivo:
# El propósito de Urban Grocers es desarrollar un sistema para generar kits con distintos productos para cada usuario que se registre,
# asignando de forma aleatoria un token, el cual guardará los datos del kit correspondiente.

# Instrucciones para realizar las pruebas:
# 1. Consultar las APIs usando las rutas URL_SERVICE, CREATE_USER_PATH y PRODUCT_KITS_PATH del registro de APIs.
# 2. Crear un nuevo perfil de usuario proporcionando los siguientes datos: 
#    body_user = { "firstName": "Max", "email": "max@example.com", "phone": "+10005555355", "comment": "test" }.
# 3. Guardar el token generado para el usuario en una variable, con el fin de utilizarlo posteriormente al crear el kit.
# 4. Generar el kit utilizando el token del usuario y almacenar la información del mismo.
# 5. Establecer los posibles resultados esperados, como códigos 201 (éxito) y 400 (error).
# 6. Definir los escenarios de prueba en función de esos valores esperados.
# 7. Ejecutar las pruebas, diferenciando entre casos válidos e inválidos.
# 8. Comprobar que los resultados coincidan con lo que se espera en cada caso.