from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NameAppConfig(AppConfig):
    name = 'nameapp'
    verbose_name = _("NameApp")
