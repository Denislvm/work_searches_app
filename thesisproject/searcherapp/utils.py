from .models import *

menu = [{'title': "О сайте", 'url_name': "about"},
        {'title': "Startup", 'url_name': "startup"},
        {'title': "Добавить вакансию", 'url_name': 'addpage'},
        {'title': "Добавить Startup", 'url_name': 'add_startup'},
        {'title': "Контакты", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(3)
            user_menu.pop(2)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context