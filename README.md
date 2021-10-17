# yt-api-task

# Project Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# ✅ Basic Requirements:

- ✅ Server should call the YouTube API continuously in background (async) with some interval (using 1 minute) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs) in a database with proper indexes.
- ✅ A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
  - endpoint: /video
  - sample query: http://127.0.0.1:8000/video/
- ✅ A basic search API to search the stored videos using their title and description.
- ✅ Dockerize the project.
  - run using docker-compose
- ✅ It should be scalable and optimised.

# Bonus Points:

- ✅ Make a dashboard to view the stored videos with filters and sorting options (optional)
