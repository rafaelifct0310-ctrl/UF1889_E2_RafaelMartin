# Simulación API
### Objetivo

Simular los datos que podrían enviarse desde Odoo hacia otro sistema meiante un API.

### Endpoint simulado

```text
POST /api/clientes/seguimientos
```

´´´json
[
    {
        "id": 9,
        "complete_name":"Acme Corporation",
        "numero_seguimientos": 3
    },
    {
        "id": 15,
        "complete_name":"Azure Interior",
        "numero_seguimientos": 0
    },
    {
        "id": 10,
        "complete_name":"Gemini Furniture",
        "numero_seguimientos": 2
    }
]
```

