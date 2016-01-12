from google.appengine.ext import ndb

# Object that represents a comment
class Comment(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    message = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)