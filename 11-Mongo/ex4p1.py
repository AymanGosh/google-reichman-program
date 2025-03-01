import feedparser

from pymongo import MongoClient

client = MongoClient()

db = client.get_database("news_db")
magazines = db.get_collection("magazine")


RSS = "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml"
# OR:
# RSS = "http://feeds.feedburner.com/PythonInsider"
# RSS = "https://news.ycombinator.com/rss"
# RSS = "http://feeds.feedburner.com/TechCrunch/"
# RSS = "https://www.jpost.com/rss/rssfeedsfrontpage.aspx"
# RSS = "http://www.ynet.co.il/Integration/StoryRss3082.xml"

d = feedparser.parse(RSS)



for n in d.entries :
    magazines.insert_one({'title':n.title , 'link':n.link , 'summary':n.summary})


cur = magazines.find()
for d in cur:
    print(d)


magazines.drop()