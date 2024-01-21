# Copyright (C) 2024 - Michel Perrocheau (https://github.com/myrrkel).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _compute_im_status(self):
        super(ResPartner, self)._compute_im_status()
        ai_bot_user_id = self.env['ir.model.data']._xmlid_to_res_id('mistralai_chat.partner_ai')
        for user in self.filtered(lambda u: u.id == ai_bot_user_id):
            user.im_status = 'online'
