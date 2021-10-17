from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Video
import asyncio
from .yt_session import getListVideos

def delete_videos_database():
    Video.objects.all().delete()

def add_to_database(res):
    for v in res:
        snippet = v['snippet']
        formated_date = snippet['publishedAt']
        vid = Video(title= snippet['title'], description= snippet['description'], publishTime= formated_date, thumbnail_url= snippet['thumbnails']['medium']['url'], url= v['id']['videoId'], channelTitle=snippet['channelTitle'])
        print("Added:",vid.title)
        vid.save()

def sort_filter_videos(filter='',sort_by=''):
    if sort_by == '' and filter == '':
        return Video.objects.all()
    elif sort_by != '' and filter == '':
        return Video.objects.order_by(sort_by)
    elif sort_by == '' and filter != '':
        return Video.objects.filter(Q(title__icontains=filter) | Q(description__icontains=filter))
    else:
        return Video.objects.filter(Q(title__icontains=filter) | Q(description__icontains=filter)).order_by(sort_by)
    
    
def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def refresh_loop(keyword):
    while(True):
        print("Refreshed!")
        data = getListVideos(keyword)
        add_to_database(data)
        # Refresh the database every 10 s
        await asyncio.sleep(10)
        
# def drop_table(self):
#     cursor = connection.cursor()
#     table_name = self.model._meta.db_table
#     sql = "DROP TABLE %s;" % (table_name, )
#     cursor.execute(sql)
