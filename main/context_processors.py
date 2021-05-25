#-*- coding: utf-8 -*-


def current_town(request):
    return {'current_town': request.current_town}


def moder_panel(request):
    return {
        'is_moder': request.is_moder,
        'is_client': request.is_client
    }
