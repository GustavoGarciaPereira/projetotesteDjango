from django.conf import settings
from datetime import datetime


# class TesteMiddleware:
#     def process_request(self, request):
#         # request.session['data_hora'] = datetime.now()
#         pass

class TesteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request.session['data_hora'] = str(datetime.now())
        request.session['nome'] = "gustavo"
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response