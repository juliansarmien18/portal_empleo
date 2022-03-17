# portal_empleo
Prueba sobre un Portal básico de empleo usando Django Rest Framework

Se contemplan 5 modelos relacionados

DocumentType: para definir los tipos de documento que podra seleccionar un usuario al registrarse

Offers: Las ofertas que se crearán y listaran para los usuarios

Postulation: La postulacion que relaciona un usuario a una oferta

Status: tabla paramétrica que contiene los estados posibles de una oferta

UserApp: datos adicionales al usuario en si, se relaciona con la tabla auth_user


Se utiliza el metodo de autenticación TokenAuthtentication para cumplir con las reglas del negocio

la app core contiene una carpeta llama api donde se encuentran las vistas, los serializadores, las funciones y las urls,

En functions.py se aloja la funcion que realiza el envío de email por consola al completarse un registro

El sistema esta configurado para que el usuario administrador pueda acceder al portal django-admin y crear usuarios, estados y tipos de documento a parte de los grupos y los usuarios predefinidos por django.
