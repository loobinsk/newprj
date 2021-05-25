# -*- coding: utf-8 -*-


class BaseExam(object):

    RESULT_AGENT = 'a'
    RESULT_OWNER = 'o'
    RESULT_UNDEFINED = 'u'

    def __init__(self):
        super(BaseExam, self).__init__()

    def test(self, tel):
        return BaseExam.RESULT_UNDEFINED

