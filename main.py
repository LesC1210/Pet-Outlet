import webapp2
import jinja2
import os 
import urllib2
import urllib
import logging

from google.appengine.ext import ndb


class User(ndb.Model):
	name = ndb.StringProperty()
	userEmail = ndb.StringProperty()
	
class Dog(ndb.Model):
	dogName = ndb.StringProperty()
	userID = ndb.StringProperty()
	age = ndb.IntegerProperty()
		
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

		dog = Dog(dogName=petname, userID=user_key.id(), age=age)
		dog_key= dog.put()




		template= jinja_environment.get_template('welcome.html')
		self.response.write(template.render(
			{
				'name': username,
				'pet_name': petname,
			}))

'''class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('welcome.html')
		self.response.write(template.render())'''

class ScheduleHandler(webapp2.RequestHandler):
	def get(self):
		username = self.request.get('username')
		logging.info(age)
		user= User.query(Username ==username).fetch()[0]
		dog= Dog.query(userID == user_key()).fetch()[0]
		age = dogAge
		age = int


		if (age < 3):
			template = jinja_environment.get_template('schedule1.html')
			self.response.write(template.render(
				{
					'petAge' : age
				}))

		elif (age < 9):
			template = jinja_environment.get_template('schedule2.html')
			self.response.write(template.render(
				{
					'petAge' : age
				}))

		else:
			template = jinja_environment.get_template('schedule3.html')
			self.response.write(template.render(
				{
					'petAge' : age
				}))


		
app = webapp2.WSGIApplication([
	('/', MainHandler),
	#('/welcome',WelcomeHandler),
	('/signup', SignUpHandler),
	('/schedule', ScheduleHandler),
], debug=True)
