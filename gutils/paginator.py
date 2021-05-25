from django.core.paginator import Paginator
import hashlib
from django.core.cache import cache


class CachedPaginator(Paginator):

    timeout = 600

    def _get_count(self):
        m = hashlib.md5()
        m.update(str(self.object_list.query))
        hash = 'page_%s' % m.hexdigest()
        if self._count is None:
            self._count = cache.get(hash, None)
        if self._count is None:
            try:
                self._count = self.object_list.count()
            except (AttributeError, TypeError):
                # AttributeError if object_list has no count() method.
                # TypeError if object_list.count() requires arguments
                # (i.e. is of type list).
                self._count = len(self.object_list)
            cache.set(hash, self._count, self.timeout)
        return self._count
    count = property(_get_count)
