/** @odoo-module */

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";

registry.category("discuss.channel_commands").add("clear_mistral", {
    help: _t("Clear chat with AI Bot"),
    methodName: "execute_command_clear_mistralai_chat",
});
