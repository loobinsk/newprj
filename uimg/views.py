# coding=utf8
from gutils.views import *
from uimg.models import *
from django.views.generic import CreateView, DeleteView, View, DetailView, UpdateView, TemplateView, ListView
from datetime import datetime
from annoying.decorators import ajax_request
from django.utils.decorators import method_decorator
from gutils.views import content_type
from uimg.forms import ImageDescForm
from django.template import loader, Context
from django.core.urlresolvers import reverse


class UserImageDeleteView(LoginRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = UserImage
    pk_url_kwarg = 'id'
    success_url = '/'

    def get_model_dict(self):
        return {}


class UserImageMultipleCreateView(AjaxableResponseMixin, View):

    @method_decorator(content_type)
    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        image_list = request.FILES.getlist('images')
        result = []
        if image_list:
            for image in image_list:
                try:
                    img = UserImage(date=datetime.now())
                    if request.user.is_authenticated():
                        img.user = request.user
                    img.image.save(image.name, image)
                    img.save()
                    result.append({
                        'id': img.id,
                        'url': img.image.url
                    })
                except:
                    pass
        return result


class UserImagePreviewView(DetailView):
    model = UserImage
    template_name = 'uimg/preview.html'
    pk_url_kwarg = 'id'
    context_object_name = 'image'


class UserImageUpdateView(LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    template_name = 'uimg/form.html'
    form_class = ImageDescForm
    model = UserImage
    pk_url_kwarg = 'id'
    context_object_name = 'image'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(UserImageUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('uimg:edit', kwargs={'id': self.object.pk})
        return context

    def get_model_dict(self):
        tpl = loader.get_template('uimg/preview.html')
        return {
            'preview': tpl.render(Context({
                'image': self.object
            }))
        }


class UserImageLibraryView(LoginRequiredMixin, TemplateView):
    template_name = 'uimg/library.html'


class UserImageLibraryListView(LoginRequiredMixin, ListView):
    model = UserImage
    template_name = 'uimg/library-list.html'
    paginate_by = 20
    context_object_name = 'image_list'

    def get_queryset(self):
        return UserImage.objects.filter(user=self.request.user).order_by('-date')


class UserImageLibraryPreviewView(UserImagePreviewView):
    template_name = 'uimg/library-preview.html'