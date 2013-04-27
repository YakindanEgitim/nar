# core/mixins.py
from django.contrib import messages


class ActionMixin(object):
    """Used to set a message for the action carried out by the view"""

    @property
    def action(self):
        msg = "{0} is missing action.".format(self.__class__)
        raise NotImplementedError(msg)

    def form_valid(self, form):
        messages.info(self.request, self.action)
        return super(ActionMixin, self).form_valid(form)


class SearchMixin(object):
    """Generic query filter for search"""

    search_mapping = {'u': 'username'}  # mapping for attributes to be searched

    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()

        q = self.request.GET.get('q')
        if q:
            typ = self.request.GET.get('t')
            if typ not in self.search_mapping.keys():
                typ = self.search_mapping.keys()[0]
            return queryset.filter(**{self.search_mapping[typ] + '__icontains': q})
        return self.model.objects.none()
