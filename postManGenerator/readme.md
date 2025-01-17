# How to use
Para usarse se debe proporcionar un fichero que contenga diversas lineas con los endpoints de la API a generar el PostMan de la siguiente manera:
```bash
/prueba1?parametro1=aaaaaaa - GET,PATCH,PUT
/prueba2?parametro2=aaaaaaa - POST,GET
/prueba3?parametro3=aaaaaaa - UPDATE
```
## A tener en cuenta
- Se debe poner el método de la petición, si no no lo incluye
- se pueden usar variables metiendolo entre {{}} y el postman guardará lo que pongas como variable.
