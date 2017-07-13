import webapp2
import jinja2
import os 
import urllib2
import urllib

from google.appengine.ext import ndb

class User(ndb.Model):
	userEmail = ndb.StringProperty()
	userPass= ndb.StringProperty()

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('pet-outlet.html')
		self.response.write(template.render())
	
class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('welcome.html')
		self.response.write(template.render())

class SignUpHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('sign_up.html')
		self.response.write(template.render())
		 
	def post(self):
		username= self.request.get('name')
		petname= self.request.get('pet_name')
		email = self.request.get('userEmail')
		password= self.request.get('userPass')
		breed = self.request.get('petbreed')
		age = self.request.get('petAge')

		template= jinja_environment.get_template('welcome.html')
		self.response.write(template.render(
			{
				'name': username,
				'pet_name': petname,
			}))

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/welcome',WelcomeHandler),
	('/signup', SignUpHandler),

], debug=True)

