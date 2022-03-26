import praw
import datetime

reddit = praw.Reddit(client_id="RJf5ores-wofqZ469uTZ7A", client_secret="h-F52yFtyLu9YPp9RIDdK5tZuPj85Q",
                    user_agent="gigwellbeing", username="woomzie", password="juno0702")

keyword = 'depression'

subreddit = reddit.subreddit('uberdrivers')

resp = subreddit.search(keyword, time_filter="year", limit=10)

for submission in resp:
   print("ID: \n", submission.id)
   print("  Title: \n", submission.title)
   print("  Body: \n", submission.selftext)
   print("  URL: ", submission.url)
