from django.shortcuts import render
from django.views.generic import TemplateView,View
import asyncio
from django.utils.decorators import classonlymethod
from .getData import main as torrentAPI
class Home(TemplateView):
    template_name = "pirate/index.html"
class Search(View):
    template_name = "pirate/search.html"
    async def get(self,request,*args,**kwargs):
        if kwargs.get("query") and len(kwargs.get("query"))>3:
            data = await torrentAPI(kwargs)
        else:
            data = None
        return render(request,self.template_name,{"results":data})
    @classonlymethod
    def as_view(cls,**initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view
class Description(View):
    template_name = "pirate/description.html"
    async def get(self,request,*args,**kwargs):
        data = await torrentAPI(kwargs)
        id = data.get("id")
        if id:
            data2 = await torrentAPI({"fileid":id})
            data["filesName"] = data2
        return render(request,self.template_name,{"result":data})
    @classonlymethod
    def as_view(cls,**initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view