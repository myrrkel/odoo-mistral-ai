# -*- coding: utf-8 -*-
# Copyright (C) 2024 - Michel Perrocheau (https://github.com/myrrkel).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, api, _
from odoo.tools import html2plaintext
from mistralai.models.chat_completion import ChatMessage

import logging

_logger = logging.getLogger(__name__)


class MistralAiCompletion(models.Model):
    _name = 'mistralai.completion'
    _description = 'MistralAI Completion'
    _inherit = ['mistralai.mixin']

    def _get_mistralai_model_list(self):
        try:
            mistralai = self.get_mistralai()
        except Exception as err:
            return [('mistral-tiny', 'mistral-tiny'), ('mistral-medium', 'mistral-medium')]
        model_list = mistralai.list_models()
        res = [(m.id, m.id) for m in model_list.data]
        res.sort()
        return res

    def _get_post_process_list(self):
        return [('list_to_many2many', _('List to Many2many')),
                ('json_to_questions', _('JSON to questions'))]

    def _get_response_format_list(self):
        return [('text', _('Text')),
                ('json_object', _('JSON Object')),
                ]

    ai_model = fields.Selection(selection='_get_mistralai_model_list', string='AI Model')
    system_template = fields.Text()
    system_template_id = fields.Many2one('ir.ui.view', string='System Template View')
    temperature = fields.Float(default=1)
    max_tokens = fields.Integer(default=16)
    top_p = fields.Float(default=1)
    test_answer = fields.Text(readonly=True)
    post_process = fields.Selection(selection='_get_post_process_list')
    response_format = fields.Selection(selection='_get_response_format_list', default='text')

    def create_completion(self, rec_id=0, messages=None, prompt='', **kwargs):
        mistralai = self.get_mistralai()
        if not messages:
            messages = []
            system_prompt = self.get_system_prompt(rec_id)
            if system_prompt:
                messages.append(ChatMessage(role='system', content=system_prompt))

            if not prompt and rec_id:
                prompt = self.get_prompt(rec_id)
            messages.append(ChatMessage(role='user', content=prompt))

        max_tokens = kwargs.get('max_tokens', self.max_tokens)
        res = mistralai.chat(
            model=self.ai_model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
        )
        prompt_tokens = res.usage.prompt_tokens
        completion_tokens = res.usage.completion_tokens
        total_tokens = res.usage.total_tokens

        result_ids = []
        for choice in res.choices:
            if rec_id:
                answer = choice.message.content
                result_id = self.create_result(rec_id, prompt, answer, prompt_tokens, completion_tokens, total_tokens)
                if self.post_process and not self.target_field_id:
                    result_id.exec_post_process(answer)
                result_ids.append(result_id)
            else:
                return [choice.message.content for choice in res.choices]
        return result_ids

    def mistralai_create(self, rec_id, method=False):
        return self.create_completion(rec_id)

    def create_result(self, rec_id, prompt, answer, prompt_tokens, completion_tokens, total_tokens):
        values = {'completion_id': self.id,
                  'model_id': self.model_id.id,
                  'target_field_id': self.target_field_id.id,
                  'res_id': rec_id,
                  'prompt': prompt,
                  'answer': answer,
                  'prompt_tokens': prompt_tokens,
                  'completion_tokens': completion_tokens,
                  'total_tokens': total_tokens,
                  }
        result_id = self.env['mistralai.completion.result'].create(values)
        return result_id

    def get_system_prompt(self, rec_id):
        context = {'html2plaintext': html2plaintext}
        return self._get_prompt(rec_id, self.system_template_id, self.system_template, context)

    def run_test_completion(self):
        rec_id = self.get_records(limit=1).id
        if not rec_id:
            return
        self.test_prompt = self.get_prompt(rec_id)
        result_ids = self.create_completion(rec_id)
        self.test_answer = result_ids[0].answer
