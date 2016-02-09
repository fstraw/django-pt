from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_project_and_retreive_it_later(self):
	## Heather wants to check out the new project tracking web app
	## She goes to check out the homepage
		self.browser.get('http://localhost:8000') 

##She sees that it is called 'EPEI Project Tracking'
		self.assertIn('EPEI Project Tracking', self.browser.title)
		self.fail('Finish the test!')

##She sees an overview of current projects, with the most pressing listed at the top

##She wants to find one of her projects in the database in the omnibox

##She wants to create a new project

##She moves on to something else
if __name__ == '__main__':
	unittest.main()