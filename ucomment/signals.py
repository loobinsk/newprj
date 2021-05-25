# -*- coding: utf-8 -*-
from django.dispatch import Signal


comment_create = Signal(providing_args=['user'])
