from googleapiclient.discovery import build
from urllib.error import HTTPError
from django.conf import settings

yt_service = build('youtube', 'v3', developerKey=settings.YOUTUBE_DATA_API_KEY)

def getListVideos(keyword:str, page_token=''):
    # Call the API
   
    req = yt_service.search().list(
        part = 'snippet',
        maxResults = '400',
        publishedAfter= '2020-01-01T00:00:00Z',
        q = keyword,
        type = 'video',
        pageToken = page_token
    )
        
    try:
       res = req.execute()
       
    except HTTPError as e:
        print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))
    return res

    

