from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_project_and_retrieve_it_later(self):
	## Heather wants to check out the new project tracking web app
	## She goes to check out the homepage
		self.browser.get('http://localhost:8000')
		##She sees that it is called 'EPEI Project Tracking'
		self.assertIn('EPEI Project Tracking', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('EPEI Project Tracking', header_text)
		##She sees an overview of current projects, with the most pressing listed at the top
		
		##She wants to find one of her projects in the database in the omnibox
		# inputbox = self.browser.find_element_by_id('id_search')
		# self.assertEqual(
			# inputbox.get_attribute('placeholder'),
			# 'Search for project'
		# )
		# She looks for an EPEI Project
		# inputbox.send_keys('PBQ1601')
		# When she presses enter, the list is filtered to just the project(s) she needs
		# inputbox.send_keys(Keys.ENTER)
		# table = self.browser.find_element_by_id('id_project_table')
		# rows = self.browser.find_elements_by_tag_name('tr')
		# self.assertTrue(
			# any(row.text == 'PBQ1601' for row in rows),
			# "New project did not appear in table"
		# )
		##She wants to create a new project. She sees a button called 'Add Project'
		add_button = self.browser.find_element_by_id('id_add')
		##She clicks the button to add a project
		add_button.click()
		##See sees that the page is called "EPEI Project Tracking - Add Project"
		self.assertIn('Add Project', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Add Project', header_text)
		# She sees fields for data entry and fills them out
		epid_input_box = self.browser.find_element_by_id('id_epid')
		epid_input_box.send_keys('PBQ1601')
		air_input_box = self.browser.find_element_by_id('id_air')
		air_input_box.send_keys('Yes')
		noise_input_box = self.browser.find_element_by_id('id_noise')
		noise_input_box.send_keys('Yes')
		ecology_input_box = self.browser.find_element_by_id('id_ecology')
		ecology_input_box.send_keys('Yes')
		archaeology_input_box = self.browser.find_element_by_id('id_archaeology')
		archaeology_input_box.send_keys('Yes')
		history_input_box = self.browser.find_element_by_id('id_history')
		history_input_box.send_keys('Yes')
		#She saves the form completely and is taken to the home page
		# save_button = self.browser.find_element_by_id('id_save_project')
		# save_button.click()
		# self.assertIn('EPEI Project Tracking', self.browser.title)
		self.fail('Finish the test!')

##She moves on to something else
if __name__ == '__main__':
	unittest.main()