from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_pyramid(request):
    print('-> solicitud entrante')
    return Response('<body><h1>Hola Pyramid</h1></body>')


def hello_you(request):
    print('-> solicitud entrante')
    return Response('<body><h1>Hola {}</h1></body>'.format(request.matchdict["name"]))


def not_found(request):
    return Response('<body><h1>P&aacute;gina no encontrada</h1></body>')



if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_route('hello_you', '/nombre/{name}')
    config.add_view(hello_pyramid, route_name='hello')
    config.add_view(hello_you, route_name='hello_you')
    config.add_notfound_view(not_found)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
