from django.shortcuts import render
from django.views.generic import TemplateView
from .extract import *
# Create your views here.


class IndexPageView(TemplateView):
    template_name = "index.html"

    def post(self,request, *args, **kwargs):
        file = request.FILES
        data = extract_img(file)
        context = {
            "data":data
        }
        return render(request, "index.html", context)



