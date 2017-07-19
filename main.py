import webapp2
import jinja2
import os 
import urllib2
import urllib
import logging

from google.appengine.ext import ndb


class User(ndb.Model):
	name = ndb.StringProperty() 
	
class Dog(ndb.Model):
	dogName = ndb.StringProperty()
	userID = ndb.IntegerProperty()
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

		logging.info(age) 
		age = int(age)

		dog = Dog(dogName=petname, userID=user_key.id(), age=age)
		dog_key= dog.put()




		template= jinja_environment.get_template('welcome.html')
		self.response.write(template.render(
			{
				'name': username,
				'pet_name': petname,
				'dog_key' : dog_key.id()
			}))

'''class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('welcome.html')
		self.response.write(template.render())'''

class ScheduleHandler(webapp2.RequestHandler):
	def get(self):
		#logging.info(age)
		dog_key = self.request.get('id')
		#dog_key = int(dog_key)
		dog_model = User.get_by_id(dog_key)
		#username = User.query(User.name == username).fetch()[0]
		logging.info(User.key.id)
		dog = Dog.query(Dog.userID == username.key.id()).fetch()[0]
		age = dog.age
		


		if (age < 3):
			template = jinja_environment.get_template('schedule1.html')
			self.response.write(template.render())

		elif (age < 9):
			template = jinja_environment.get_template('schedule2.html')
			self.response.write(template.render())

		else:
			template = jinja_environment.get_template('schedule3.html')
			self.response.write(template.render())


		
app = webapp2.WSGIApplication([
	('/', MainHandler),
	#('/welcome',WelcomeHandler),
	('/signup', SignUpHandler),
	('/schedule', ScheduleHandler),
], debug=True)
