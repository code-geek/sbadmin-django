from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "components/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'title': "Dashboard"})
        return context


class BlankView(TemplateView):
    template_name = "components/blank.html"

    def get_context_data(self, **kwargs):
        context = super(BlankView, self).get_context_data(**kwargs)
        context.update({'title': "Blank Page"})
        return context


class ButtonsView(TemplateView):
    template_name = "components/buttons.html"

    def get_context_data(self, **kwargs):
        context = super(ButtonsView, self).get_context_data(**kwargs)
        context.update({'title': "Buttons"})
        return context


class FlotView(TemplateView):
    template_name = "components/flot.html"

    def get_context_data(self, **kwargs):
        context = super(FlotView, self).get_context_data(**kwargs)
        context.update({'title': "Flot Charts"})
        return context


class FormsView(TemplateView):
    template_name = "components/forms.html"

    def get_context_data(self, **kwargs):
        context = super(FormsView, self).get_context_data(**kwargs)
        context.update({'title': "Forms"})
        return context


class GridView(TemplateView):
    template_name = "components/grid.html"

    def get_context_data(self, **kwargs):
        context = super(GridView, self).get_context_data(**kwargs)
        context.update({'title': "Grid"})
        return context


class IconsView(TemplateView):
    template_name = "components/icons.html"

    def get_context_data(self, **kwargs):
        context = super(IconsView, self).get_context_data(**kwargs)
        context.update({'title': "Icons"})
        return context


class LoginView(TemplateView):
    template_name = "components/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({'title': "Log In"})
        return context


class MorrisView(TemplateView):
    template_name = "components/morris.html"

    def get_context_data(self, **kwargs):
        context = super(MorrisView, self).get_context_data(**kwargs)
        context.update({'title': "Morris Charts"})
        return context


class NotificationsView(TemplateView):
    template_name = "components/notifications.html"

    def get_context_data(self, **kwargs):
        context = super(NotificationsView, self).get_context_data(**kwargs)
        context.update({'title': "Notifications"})
        return context


class PanelsView(TemplateView):
    template_name = "components/panels-wells.html"

    def get_context_data(self, **kwargs):
        context = super(PanelsView, self).get_context_data(**kwargs)
        context.update({'title': "Panels and Wells"})
        return context


class TablesView(TemplateView):
    template_name = "components/tables.html"

    def get_context_data(self, **kwargs):
        context = super(TablesView, self).get_context_data(**kwargs)
        context.update({'title': "Tables"})
        return context


class TypographyView(TemplateView):
    template_name = "components/typography.html"

    def get_context_data(self, **kwargs):
        context = super(TypographyView, self).get_context_data(**kwargs)
        context.update({'title': "Typography"})
        return context
