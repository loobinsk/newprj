#-*- coding: utf-8 -*-
import cProfile
import os
from django.conf import settings


def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = os.path.join(settings.BASE_DIR, 'profile', func.__name__ + '.prof')
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper