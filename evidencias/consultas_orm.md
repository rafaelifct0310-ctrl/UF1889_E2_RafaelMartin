# Consulta ORM
### Objetivo

Obtener el número de seguimientos comerciales realizadas

##### Agrupa las actividades (mail.activity) por cliente (res_id)
        
```python
grouped_data = self.env["mail.activity"].read_group(
    domain=[
        ("res_model","=","res.partner"),
        ("res_id","in",self.ids),
    ],
    fields=["res_id"],
    groupby=["res_id"],
)
```
