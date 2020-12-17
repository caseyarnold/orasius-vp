from django.contrib.auth.decorators import login_required
from auths.models import Profile

class LoginRequiredMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not getattr(view_func, 'login_required', True):
            return None
        return login_required(view_func)(request, *view_args, **view_kwargs)


class UpdateLastSeenMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated():
            return Profile.objects.filter(user=request.user).first().save()
