import configuration
import requests
import data


def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json= data.user_body, #inserta el cuerpo de la solicitud
                         headers= data.headers_user) # inserta los encabezados

def post_create_kit(a):

    token = post_new_user().json()

    h = data.headers_kit.copy()
    h['Authorization'] = 'Bearer ' + token['authToken']

    #Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, #Concatenamos la URl y buscando el API en el Producto
                         json= a, #Datos a enviar en la solicitud
                         headers= h) #Encabezados de solicitud


r = post_create_kit(data.kit_body_2)
print(r.status_code)
print(r.json())


