# UF1889
## Identificar modelos de clientes
- Clientes -> res.partner  (almacena clientes)
- Seguimientos -> mail.activity  (almacena actividades/seguimientos)

### Modelo de clientes
`res.partner`

Campos útiles:
- `name`
- `email`
- `phone`
- `is_company`
- `customer_rank`
- `active`

### Modelo de seguimientos
`mail.activity`

Campos útiles:
- `res_model`
- `res_id`
- `activity_type_id`
- `summary`
- `date_deadline`
- `user_id`
- `create_date`

### Relación entre modelos

- En `mail.activity`, el registro apunta a un modelo y a un identificador
- cuando `res_model = 'res_partner'`, y `res_id` coincide con el id del cliente, esa pertenece a a ese cliente.

###   
