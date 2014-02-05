import os
import webapp2
import jinja2

from google.appengine.ext import db
from google.appengine.api import memcache
import time
import random
import string
import hashlib
import logging
import json

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape= True)

class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
    self.response.out.write(*a, **kw)
  def render_str(self, template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)
  def render(self, template, **kw):
    self.write(self.render_str(template, **kw))



class MainPage(Handler):
  def render_front(self):
    #posts = get_front()
    #age = time.time() - memcache.get("age")
    self.render("front.html")

  def json_front(self):
    posts = get_front()

    self.response.headers["Content-Type"] = "application/json"
    lp = [BlogPostEncoder().encode(p) for p in posts]

    j = json.dumps([json.loads(p) for p in lp])

    self.response.write(j)
    
  def get(self):
    format = ''
    if format and format == '.json':
      self.json_front()
      return
    self.render_front()


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)