El servicio de registro es el encargado de registrar todos los dispositivos en nuestro sistema y por tanto saber su ubicacion y el tipo de dispositivo que es.
Dispondrá de las tipicas operaciones CRUD las cuales se operaran a traves de un API REST.
# Servicio de registro de dispositivos.

## Utilizacion

Todas las respuestas tendran la forma siguiente:

```json
{
    "data": "Tipo mixto que contiene la informacion de la respuesta",
    "mensaje": "Descripcion de lo que ha ocurrido"
}
```

Las respuestas de mensaje solamente van a añadir detalle de la operacion realizada en el campo 'data'.

### Lista de todos los dispositivos

**Definiciones**

`GET /devices`

**Respuestas**

- `200 OK` on success, resultado satisfactorio.
```json
[
    {
        "identificador": "lampara-entrada",
        "nombre": "Lampara de la entrada",
        "tipo_dispositivo": "lampara",
        "gateway_controlador": "192.168.1.135"
    },
    {
        "identificador": "samsung-smartTv",
        "nombre": "Television Samsung Salon",
        "tipo_dispositivo": "tv",
        "gateway_controlador": "192.168.1.102"
    }
]
 ```

 ### Registrando nuevos dispositivos

 **Definiciones**

 `POST /devices`

 **Argumentos**
 - `"identificador": string` un identificador global y único para el dispositivo.
 - `"nombre": string` un nombre amigable para el dispositivo.
 - `"tipo_dispositivo": string` el tipo de dispositivo.
 - `"gateway_controlador": string` la direccion IP de la puerta de enlace.

 Si el dispositivo con el identificador dado ya existe, los datos de este se sobreescribiran.

 **Respuestas**

 - `201 Created` on success

 ```json
{
    "identificador": "lampara-entrada",
    "nombre": "Lampara de la entrada",
    "tipo_dispositivo": "lampara",
    "gateway_controlador": "192.168.1.135"
}
```

### Obtener detalles de un dispositivo

`GET /device/<identificador>`
**Respuestas**

- `404 Not Found` si el dispositivo no existe.
- `200 OK` on success.

```json
{
    "identificador": "lampara-entrada",
    "nombre": "Lampara de la entrada",
    "tipo_dispositivo": "lampara",
    "gateway_controlador": "192.168.1.135"
}
```

### Borrando un dispositivo

**Definiciones**

`Delete /devices/<identificador>`

**Respuesta**

- `404 Not Found` si el dispositivo no existe
- `204 No Content` la accion se ha llevado a cabo correctamente.