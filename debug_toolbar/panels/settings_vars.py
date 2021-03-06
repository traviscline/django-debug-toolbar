from django.conf import settings
from django.template.loader import render_to_string
from django.views.debug import get_safe_settings
from debug_toolbar.panels import DebugPanel

class SettingsVarsDebugPanel(DebugPanel):
    """
    A panel to display all variables in django.conf.settings
    """
    name = 'SettingsVars'
    has_content = True

    def title(self):
        return 'Settings'

    def url(self):
        return ''

    def content(self):
        context = self.to_data()
        return render_to_string('debug_toolbar/panels/settings_vars.html', context)

    def to_data(self):
        return { 'settings': get_safe_settings() }