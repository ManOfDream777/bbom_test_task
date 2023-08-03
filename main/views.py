from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
from .models import MyUser, Post

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['users'] = MyUser.objects.all()
        return context

class Posts(TemplateView):
    template_name = 'posts.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context = self.get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user__id = kwargs.get('id'))
        context['author'] = MyUser.objects.filter(id = kwargs.get('id')).first()
        return self.render_to_response(context)