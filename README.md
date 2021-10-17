# yt-api-task

# Project Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# ✅ Basic Requirements:

- ✅ Server should call the YouTube API continuously in background (async) with some interval (using 1 minute) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs) in a database with proper indexes.
- ✅ A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
  - endpoint: /api/video
  - sample query: http://localhost/api/video?p=2&s=3
- ✅ A basic search API to search the stored videos using their title and description.
  - endpoint: /api/video/search
  - sample query: http://localhost/api/video/search?s=music&p=2&s=3
- ✅ Dockerize the project.
  - run using docker-compose
- ✅ It should be scalable and optimised.

# Bonus Points:

- ✅ Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
  - can cycle through multiple API keys when current key gets exhausted
- 🚧 Make a dashboard to view the stored videos with filters and sorting options (optional)
- ✅ Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
  - using industry standard elastic search with full text search and partial match capabilities

# Instructions

Pre-requisites: docker and docker compose installed.

- Clone the repo `git clone https://github.com/cryptus-neoxys/yt-api-task.git`
- Open directory in terminal `cd yt-api-task`
- copy .env file `cp .env.example .env`
- Add the API KEYS in .env file
- Run docker compose `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d`
- Project should be running via nginx proxy on `PORT:80` (default http port)
- Go to http://localhost/api
- To stop the project run `docker-compose -f docker-compose.yml -f docker-compose.dev.yml down`

## API

- `GET`
  - endpoint: /api/video
  - response: `{data: []video, success: bool, pageNumber: int, pageSize: int, hasNext: bool, total: int}`
  - sample query: http://localhost/api/video?p=2&s=3
  - query params:

| param | for         | required | type |
| ----- | ----------- | -------- | ---- |
| p     | page number | true     | int  |
| s     | page size   | true     | int  |

- `SEARCH`
  - endpoint: /api/video/search
  - response: `{data: []video, success: bool, pageNumber: int, pageSize: int, hasNext: bool, total: int}`
  - sample query: http://localhost/api/video/search?s=music&p=2&s=3
  - query params:

| param | for         | required | type   |
| ----- | ----------- | -------- | ------ |
| p     | page number | true     | int    |
| s     | page size   | true     | int    |
| q     | search term | true     | string |
