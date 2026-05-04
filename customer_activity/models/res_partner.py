#Importar modulos necesarios
from odoo import api, field, models

#definir la clase que hereda el modelo res.partner
class ResPartner(models.Model):
    # indica que estamos extendiendo un modelo existente, no creando uno nuevo
    _inherit = "res.partner"

    # Definir un nuevo campo entero
    activity_followup_count = field.Integer(
        string="Nº de seguimientos",
        compute="_compute_activity_followup_count",
        store=False,
    )

    @api.depends("activity_ids")
    def _compute_activity_followup_count(self):
        # Agrupa las actividades (mail.activity) por cliente (res_id)
        grouped_data = self.env["mail.activity"].read_group(
            domain=[
                ("res_model","=","res.partner"),
                ("res_id","in",self.ids),
            ],
            fields=["res_id"],
            groupby=["res_id"],
        )

        # Construimos un diccionario
        counts_by_partner = {
            item["res_id"]:item["res_id_count"]
            for item in grouped_data
        }

        # Recorremos cada cliente del recorset actual
        for partner in self:
            # si no tiene actividad se le asigna 0
            partner.activity_followup_count = counts_by_partner.get(partner.id, 0)