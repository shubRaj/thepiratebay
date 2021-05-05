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
        if kwargs.get("query"):
            data = await torrentAPI(kwargs)
            if data:
                 for single in data:
                    if single["size"]>1024:
                        single["size"] = f"{round(single['size']/1024,2)} GB"
                    else:
                        single["size"] = f"{single['size']} MB"
        else:
            data = None
        return render(request,self.template_name,{"results":data})
    @classonlymethod
    def as_view(cls,**initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view