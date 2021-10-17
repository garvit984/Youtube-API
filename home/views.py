import asyncio
from threading import Thread
from django.core import paginator
from django.shortcuts import render
#from fam_django.home.document import VideoDocument
from .yt_session import getListVideos
from .models import Video
from .managedatabase import *
from django.core.paginator import Paginator  
from django.http import JsonResponse
import json
#from elasticsearch_dsl.query import MultiMatch
user_search_data=''
def home(request):
    context = {}
    sortby = '-publishTime'
    if request.GET.get('sortby') == '':
        sortby = request.GET.get('sortby')
    if request.method == "POST":
        
        # Clear the database
        #delete_videos_database()
        #Search field
        user_search_data = request.POST['searched']
        
        # Let us access in the template, info of each video
        #data = getListVideos(user_search_data)
        
        # Sorting   
        #res = data['items']
        # Add to database
        #add_to_database(res)
        # Database Paginator
        paginator_ = Paginator(sort_filter_videos(filter=user_search_data,sort_by=sortby), 12)
        page = request.GET.get('page')
        video_build_list = paginator_.get_page(page)
        loop = asyncio.new_event_loop()
        t = Thread(target=start_background_loop, args=(loop,), daemon=True)
        t.start()
        
        task = asyncio.run_coroutine_threadsafe(refresh_loop(user_search_data), loop)
        context = {
        'videos': video_build_list,
        'video_build_list': video_build_list,
        'searched': user_search_data,
        }
        #q = request.GET.get('q')
        #if q:
        #    query = MultiMatch(query=q, fields=['title', 'description'])
        #video = Video.objects.filter(title__icontains=user_search_data, description__icontains=user_search_data)
        return render(request, 'home/home.html', context)
    else:
        # Database Paginator
        paginator_ = Paginator(sort_filter_videos(sort_by=sortby), 12)
        page = request.GET.get('page')
        video_build_list = paginator_.get_page(page)        
        context = {
        'videos': video_build_list,
        'video_build_list': video_build_list,
        }
        return render(request, 'home/home.html', context)

def getVideo(request):
    video = list(Video.objects.order_by('-publishTime').values())
    return JsonResponse(video, safe=False)

