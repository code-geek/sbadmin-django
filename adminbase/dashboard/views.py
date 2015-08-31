from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "components/index.html"


class BlankView(TemplateView):
    template_name = "components/blank.html"


class ButtonsView(TemplateView):
    template_name = "components/buttons.html"


class FlotView(TemplateView):
    template_name = "components/flot.html"


class FormsView(TemplateView):
    template_name = "components/forms.html"


class GridView(TemplateView):
    template_name = "components/grid.html"


class IconsView(TemplateView):
    template_name = "components/icons.html"


class LoginView(TemplateView):
    template_name = "components/login.html"


class MorrisView(TemplateView):
    template_name = "components/morris.html"


class NotificationsView(TemplateView):
    template_name = "components/notifications.html"


class PanelsView(TemplateView):
    template_name = "components/panels-wells.html"


class TablesView(TemplateView):
    template_name = "components/tables.html"


class TypographyView(TemplateView):
    template_name = "components/typography.html"
