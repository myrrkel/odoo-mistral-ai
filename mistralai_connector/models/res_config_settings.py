# -*- coding: utf-8 -*-
# Copyright (C) 2022 - Michel Perrocheau (https://github.com/myrrkel).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mistralai_api_key = fields.Char(string="MistralAI API Key", config_parameter='mistralai_api_key')
    mistralai_organization_id = fields.Char(string="MistralAI Organisation ID", config_parameter='mistralai_organization_id')
