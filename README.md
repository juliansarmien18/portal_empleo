# portal_empleo
Prueba sobre un Portal básico de empleo en django implementando django-restframework

Se contemplan 5 modelos:

DocumentType: para los tipos de documentos

Status: para definir los estados de las ofertas

Offers: para la creación y actualización de ofertas

Postulation: para la creación de postulaciones

UserApp: para complementar los datos de auth_user, tiene una llave foranea a esta tabla

Se utiliza el metodo de autenticación Token Authtentication para dar cumplimiento con la lógica del negocio

El proyecto tiene una app llamada core, dentro de esta app se encuentra la carpeta api, que contiene las vistas, las urls, los serializadores y las funciones,
en el archivo functions.py se encuentra la función para enviar email por consola en el registro de un usuario.

El sistema esta configurado para que el administrador pueda crear y modificar tipos de document, usuarios, ofertas y estados a su gusto.

La mayoría de vistas se construyeron usando ModelViewSets para facilitar los servicios que parten de modelos en su mayoría, tambien se creo un serializador personalizado para dar cumplimiento a la obtención del token.
