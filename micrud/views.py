# Create your views here.
#from django.db.models import Q
from django.contrib import auth
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from models import Agenda
################################################################################
def consulta(request):
	if request.user.is_authenticated():
		consulta = request.GET.get('q', '') 
		if consulta:
			results=Agenda.objects.filter(pais=consulta).order_by('id')
			return render_to_response("consulta.html", { "results": results,"consulta": consulta})	
		return render_to_response("consulta.html", { "results": [],"consulta": consulta})	
	else:
		return HttpResponseRedirect("/nologin")			
##############################################################################
def combo(request):
	query = request.GET.get('q', '') 
	elementos= Agenda.objects.values('pais').distinct()
	if query:
		results=Agenda.objects.filter(pais=query)
		return render_to_response("consulta_combo.html",{"results": results,"query": 			query,"elementos": elementos} )
	return render_to_response("consulta_combo.html",{"results": elementos,"query": 	query,"elementos": elementos} )			
################################################################################
def agregar_registro(request):
	nom = request.GET.get('nom','')
	ape = request.GET.get('ape','')
	pais = request.GET.get('pais','')
	correo = request.GET.get('correo','')
	if nom:
		if ape:
			if pais:
				if correo:
					p=Agenda(nombre=nom,apellido=ape,pais=pais,correo=correo)
					p.save()
					return render_to_response('agregar.html',{"exito":True})							
	else:
		return render_to_response('agregar.html')
################################################################################
def eliminar_registro(request):
	cod=request.GET.get('codigo','')
	results=Agenda.objects.all().order_by('id')
	if cod:
		p = Agenda.objects.get(id=cod)
		p.delete()
		return render_to_response('eliminar.html',{"results": results,"cod":cod,"exito":True})
	return render_to_response('eliminar.html',{"results": results})	
########################################################################################
def actualizar_registro(request): 
	id = request.GET.get('id','')
	results=Agenda.objects.all().order_by('id')
	if id: # si solo obtengo el id , mostrar el detalle
		if not request.GET.get('nom',''):
			if not request.GET.get('ape',''):
				if not request.GET.get('pais',''):
					if not request.GET.get('correo',''):
						results=Agenda.objects.filter(id=id).order_by('id')
						return render_to_response('ver_detalle.html',{"results":results})	 
	if id:
		if  request.GET.get('nom',''):
			if request.GET.get('ape',''):
				if request.GET.get('pais',''):
					if request.GET.get('correo',''):
						p=Agenda.objects.get(id=request.GET.get('id',''))# Que registro va a actualizar
						p.id=request.GET.get('id','')
						p.nombre=request.GET.get('nom','')
						p.apellido=request.GET.get('ape','')
						p.pais=request.GET.get('pais','')
						p.correo=request.GET.get('correo','')		
						p.save()	
						results=Agenda.objects.all().order_by('id')	
						return render_to_response('actualizar.html',{"results":results,"id":id,"exito":True})					
	return render_to_response('actualizar.html',{"results":results}) 		
########################################################################################
def login(request):
	if request.POST.get('username',''):
		if request.POST.get('password',''):
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				# Correct password, and the user is marked "active"
				auth.login(request, user)
				# Redirect to a success page.
				return HttpResponseRedirect("/agregar")
			else:		
				# Show an error page
				return HttpResponseRedirect("/nologin")
	return render_to_response('login.html',{"login":True})	
		
def logout(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect("/login")

def nologin(request):
		return render_to_response('nologueado.html',{"error":True}) 	
