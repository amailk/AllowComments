import webapp2
from google.appengine.ext import ndb

from handler import Handler
from comment import Comment

DEFAULT_KEY = ndb.Key('KEY', "DEFAULT_KEY")

class PageHandler(Handler):

    # Status for the most recently added comment to be valid or invalid
    invalid = False

    def get(self):

        # Get all the comments, sorted by date
        comment_query = Comment.query(ancestor=DEFAULT_KEY).order(-Comment.date)
        comments = comment_query.fetch()

        self.render("main.html", comments=comments, invalid=PageHandler.invalid)

class CommentHandler(Handler):
    def post(self):
        message = self.request.get("message")
        name = self.request.get("name")

        # Check if the message is valid or invalid
        if len(message.strip()) == 0:
            PageHandler.invalid = True
        else:
            PageHandler.invalid = False

            # create a new comment object
            # set a message and name to it
            new_comment = Comment(parent=DEFAULT_KEY)
            new_comment.message = message
            new_comment.name = name

            # Save in the data-store
            new_comment.put()

        self.redirect("/")

# https://webapp-improved.appspot.com/guide/routing.html
app = webapp2.WSGIApplication([
        ("/add_comment", CommentHandler),
        ("/", PageHandler)
    ], debug=True)
