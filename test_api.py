from googleapiclient.discovery import build

API_KEY = "YOUR_API_KEY"
youtube = build("youtube", "v3", developerKey=API_KEY)

request = youtube.channels().list(
    part="snippet,statistics",
    id="UCX6OQ3DkcsbYNE6H8uQQuVA"
)

response = request.execute()



data = response["items"][0]

channel_name = data["snippet"]["title"]
subscribers = data["statistics"]["subscriberCount"]
views = data["statistics"]["viewCount"]
videos = data["statistics"]["videoCount"]

print("Channel:", channel_name)
print("Subscribers:", subscribers)
print("Views:", views)
print("Videos:", videos)

#connecting SQL

import mysql.connector
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7297897821",
    database="youtube_project"
)

cursor = conn.cursor()

# Insert query
insert_query = """
INSERT INTO channel_stats
(channel_name, subscribers, total_views, total_videos, collected_at)
VALUES (%s, %s, %s, %s, %s)
"""

values = (
    channel_name,
    int(subscribers),
    int(views),
    int(videos),
    datetime.now()
)

cursor.execute(insert_query, values)
conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()