from django.conf.urls.defaults import *
import settings
urlpatterns = patterns('',
	(r'^buscar/$','miproyecto.micrud.views.consulta'),
    (r'^combo/$','miproyecto.micrud.views.combo'), 
    (r'^agregar/$','miproyecto.micrud.views.agregar_registro'),
    (r'^eliminar/$','miproyecto.micrud.views.eliminar_registro'),
    (r'^actualizar/$','miproyecto.micrud.views.actualizar_registro'),
    (r'^login/$', 'miproyecto.micrud.views.login'),
	(r'^logout/$', 'miproyecto.micrud.views.logout'),
	(r'^nologin/$', 'miproyecto.micrud.views.nologin'),
    
    (r'css/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT + 'templates/css'}),
    
    (r'js/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_ROOT + 'templates/js'}),
    # Example:
    # (r'^miproyecto/', include('miproyecto.foo.urls')),

    # Uncomment this for admin:
	#(r'^admin/', include('django.contrib.admin.urls')),
)
