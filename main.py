import webapp2

from handler import Handler
from comment import Comment

comments = []

class PageHandler(Handler):
    def get(self, page="main.html"):
        self.render(page, comments=comments, page=page)

class CommentHandler(Handler):
    def post(self):
        message = self.request.get("message")
        name = self.request.get("name")
        page = self.request.get("page")

        new_comment = Comment(name, message)

        comments.append(new_comment)

        self.redirect("/")

# https://webapp-improved.appspot.com/guide/routing.html
app = webapp2.WSGIApplication([
        ("/add_comment", CommentHandler),
        ("/", PageHandler)
    ], debug=True)
