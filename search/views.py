from django.shortcuts import render
from django.http import *
import json
from django.views.decorators.csrf import *
from models import *
import ipdb


def response(status, msg, *args):
	# args are tuples
	res = {}
	res['status'] = status
	res['msg'] = msg
	for arg in args:
		res[arg[0]] = arg[1]
	return HttpResponse(json.dumps(res))

def home(request):
	return render(request, "search.html")


def query(request):
	q = request.GET.get("q")
	fnames = Names.objects.filter(firstname__istartswith=q)[:5]
	lnames = Names.objects.filter(lastname__istartswith=q)[:5]
	fn = []
	ln = []
	for f in fnames:
		fn.append(f.__str__())
	for l in lnames:
		ln.append(l.__str__())
	return response("success", "ok", ("last_names", ln), ("first_names", fn))