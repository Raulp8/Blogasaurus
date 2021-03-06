import webapp2
import os
import jinja2

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template=jinja_current_dir.get_template('my_blog.html')
        self.response.write(template.render())

class AboutMeHandler(webapp2.RequestHandler):
    def get(self):
        template2=jinja_current_dir.get_template('about_me.html')
        self.response.write(template2.render())

class PostHandler(webapp2.RequestHandler):
    def get(self):
        template3=jinja_current_dir.get_template('post.html')
        self.response.write(template3.render())

app = webapp2.WSGIApplication([
    ('/static', MainHandler),
    ('/aboutme', AboutMeHandler),
    ('/post', PostHandler)
], debug=True)
