from django.conf import settings
from social_auth.db.django_models import UserSocialAuth
from django.db import models
from django.contrib.sites.models import Site


@classmethod
def get_social_auth(cls, provider, uid):
    try:
        return cls.objects.select_related('user').get(provider=provider,
                                                      uid=uid,
                                                      user__site_id=settings.SITE_ID)
    except UserSocialAuth.DoesNotExist:
        return None

UserSocialAuth.get_social_auth = get_social_auth
UserSocialAuth.add_to_class('site', models.ForeignKey(Site, default=None, blank=True, null=True))
UserSocialAuth._meta.unique_together = (('provider', 'uid', 'site'),)


class UserSocialAuthManager(models.Manager):
    def get_queryset(self):
        return UserSocialAuth.admin_objects.filter(site=settings.SITE_ID)

UserSocialAuth.admin_objects = UserSocialAuth.objects
UserSocialAuth.objects = UserSocialAuthManager()


def save_social_auth(self, *args, **kwargs):
    if not self.site:
        self.site = Site.objects.get_current()
    return super(UserSocialAuth, self).save(*args, **kwargs)

UserSocialAuth.save = save_social_auth


