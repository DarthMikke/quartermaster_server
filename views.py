# Create your views here.
import os
import json

from .models import *

from django.http import JsonResponse, Http404, HttpResponseBadRequest, HttpResponseServerError, HttpResponseServerError
from django.views import View


class Categories(View):
    def get(self, request):
        categories = get_entities("categories")
        response = JsonResponse(categories, safe=False)

        response['Access-Control-Allow-Origin'] = "*"
        return response

    def put(self, request):
        # Validate the request
        new_category = json.loads(request.body)
        if not ('name' in new_category.keys()):
            return HttpResponseBadRequest

        added = put_entity("categories", new_category)

        response = JsonResponse(added, safe=False)

        response['Access-Control-Allow-Origin'] = "*"
        return response


class SingleCategory(View):
    def patch(self, request, cid):
        # Validate the request
        new_category = json.loads(request.body)
        if not ('name' in new_category.keys()):
            return HttpResponseBadRequest

        new_category['id'] = cid
        patched = patch_entity("categories", new_category)

        response = JsonResponse(patched, safe=False)

        response['Access-Control-Allow-Origin'] = "*"
        return response

    def delete(self, request, cid):
        deleted = delete_entity("categories", {'id': cid})

        response = JsonResponse(deleted, safe=False)

        response['Access-Control-Allow-Origin'] = "*"
        return


class Things(View):
    def get(self, request):
        things = get_entities("things")
        response = JsonResponse(things, safe=False)

        response['Access-Control-Allow-Origin'] = "*"
        return response

    def put(self, request):
        # Validate the request
        new_thing = json.loads(request.body)
        try:
            Thing.validate(new_thing)
        except:
            return HttpResponseBadRequest

        added = put_entity("things", new_thing)

        response = JsonResponse(added, safe=False)

        response['Access-Control-Allow-Origin'] = "*"
        return response


class SingleThing(View):
    def patch(self, request, tid):
        patch = json.loads(request.body)

        patch['id'] = tid
        patched = patch_entity("things", patch)

        response = JsonResponse(patched, safe=False)

        response['Access-Control-Allow-Origin'] = "*"
        return response

    def delete(self, request, tid):
        deleted = delete_entity("things", {'id': tid})

        response = JsonResponse(deleted, safe=False)

        response['Access-Control-Allow-Origin'] = "*"
        return response
