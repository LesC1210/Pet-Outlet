import webapp2
import jinja2
import os 
import urllib2
import urllib

from google.appengine.ext import ndb


class User(ndb.Model):
	name = ndb.StringProperty()
	userEmail = ndb.StringProperty()
	userPass= ndb.StringProperty()
	
class Dog(ndb.Model):
	dogName = ndb.StringProperty()
	breed = ndb.StringProperty()
		
jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('pet-outlet.html')
		self.response.write(template.render())
	
'''class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('welcome.html')
		self.response.write(template.render())'''

class SignUpHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('sign_up.html')
		self.response.write(template.render())
		 
	def post(self):
		username= self.request.get('name')
		petname= self.request.get('pet_name')
		email = self.request.get('userEmail')
		breed = self.request.get('petbreed')
		age = self.request.get('petAge')

		new_user = User(name = username)
		user_key = new_user.put()

		template= jinja_environment.get_template('welcome.html')
		self.response.write(template.render(
			{
				'name': username,
				'pet_name': petname,
				'email': email,
			}))
class GetScheduleHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('get_sch.html')
		self.response.write(template.render())
		 

class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('welcome.html')
		self.response.write(template.render())

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/welcome',WelcomeHandler),
	('/signup', SignUpHandler),
	('/get_sch', GetScheduleHandler),
], debug=True)
