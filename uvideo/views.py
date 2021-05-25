# coding=utf8
from gutils.views import *
from uvideo.models import *
from django.views.generic import CreateView, DeleteView
from datetime import datetime
from uvideo.forms import UserVideoForm


class UserVideoCreateView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = UserVideo
    form_class = UserVideoForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = datetime.now()

        if form.instance.get_video_source_type() == UserVideo.VIDEO_YOUTUBE:
            if not form.instance.youtube_video_id():
                raise Exception(u'Код видео Youtube не обнаружен')

        form.instance.download_thumb()
        return super(UserVideoCreateView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': self.object.image.url if self.object.image else '/static/uvideo/img/empty-video.jpg'
        }


class UserVideoDeleteView(LoginRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = UserVideo
    pk_url_kwarg = 'id'
    success_url = '/'

    def get_model_dict(self):
        return {}


