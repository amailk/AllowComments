import webapp2

from handler import Handler

class MainPage(Handler):
    def get(self):
        self.write("Allow Comments")

class AmaPage(Handler):
    def get(self):
        self.write("This is Ama")

app = webapp2.WSGIApplication([
        ("/ama", AmaPage), 
        ("/", MainPage)], debug=True)
