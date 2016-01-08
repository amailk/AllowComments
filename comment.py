from google.appengine.ext import ndb

class Comment(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    message = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)