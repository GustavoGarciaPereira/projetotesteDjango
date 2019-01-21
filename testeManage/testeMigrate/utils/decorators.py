from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings


class LoginRequiredMixin(object):
    @classmethod
    def as_view(self, **initkwargs):
        view = super(LoginRequiredMixin, self).as_view(**initkwargs)
        return login_required(view)


class StaffRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(
                request,
                'Você não tem permissão para acessar esta área.'
                'requested operation.')
            return redirect('home')
        return super(StaffRequiredMixin, self).dispatch(request,
            *args, **kwargs)


class EnfermeiroRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'ENFERMEIRO':
            messages.error(
                request,
                'Você não tem permissão para acessar esta área.'
                'requested operation.')
            return redirect('home')
        return super(EnfermeiroRequiredMixin, self).dispatch(request,
            *args, **kwargs)


class ClienteRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'CLIENTE':
            messages.error(
                request,
                'Você não tem permissão para acessar esta área.'
                'requested operation.')
            return redirect('home')
        return super(ClienteRequiredMixin, self).dispatch(request,
            *args, **kwargs)