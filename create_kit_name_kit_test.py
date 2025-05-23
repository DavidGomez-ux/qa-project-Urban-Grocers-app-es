import configuration
import data
import requests
import sender_stand_request

def postive_assert(a):
    user_body = data.kit_body.copy()
    user_body["name"] = a["name"]
    user_response = sender_stand_request.post_create_kit(a)
    assert user_response.status_code == 201

def negative_assert(b):
    user_body = data.kit_body.copy()
    user_body["name"] = b["name"]
    response = sender_stand_request.post_create_kit(b)
    assert response.status_code == 400

# Prueba 1. El número permitido de caracteres (1)
def test_create_user_1_letter():
    postive_assert(data.kit_body_1)

# Prueba 2. El número permitido de caracteres (511)
def test_create_user_511():
    postive_assert(data.kit_body_2)

# Prueba 3. Error. 	El número de caracteres es menor que la cantidad permitida (0)
def test_create_user_0():
    negative_assert(data.kit_body_3)

# Prueba 4. Error. El número de caracteres es mayor que la cantidad permitida (512)
def test_create_user_512():
    negative_assert(data.kit_body_4)

# Prueba 5. Se permiten caracteres especiales
def test_create_user_character_specials():
    postive_assert(data.kit_body_5)

# Prueba 6. Se permiten espacios:
def test_create_user_allowed_space_():
    postive_assert(data.kit_body_6)

# Prueba 7. Se permiten números:
def test_create_user_allowed_number():
    postive_assert(data.kit_body_7)

# Prueba 8. Error. 	El parámetro no se pasa en la solicitud
def test_create_user_no_params():
    negative_assert(data.kit_body_8)

# Prueba 9. Error. 	Se ha pasado un tipo de parámetro diferente (número):
def test_create_user_not_allowed_number():
    negative_assert(data.kit_body_9)