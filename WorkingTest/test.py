from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



	def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('list_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
      	               raise e                  
                   time.sleep(0.5)  
                 
	def setUp(self):
	 self.browser = webdriver.Firefox()
	def test_browser_title(self):
	 self.browser.get('http://localhost:8000/')
	 #self.browser.get(self.live_server_url)
	 self.assertIn('Job Finder',self.browser.title)
	 header_text = self.browser.find_element_by_tag_name('h1').text
	 self.assertIn('Company', header_text)
	 
	 
	 
	
	 inputCompny = self.browser.find_element_by_id('Compny')
	 self.assertEqual(inputCompny.get_attribute('placeholder'),'Company')
	 inputCompny.click()
	 time.sleep(1)
	 inputCompny.send_keys('Jollibee')
	 time.sleep(1)

	 inputAddres = self.browser.find_element_by_id('Addres')
	 self.assertEqual(inputAddres.get_attribute('placeholder'),'Address')
	 inputAddres.click()
	 time.sleep(1)
	 inputAddres.send_keys('Jollibee,Imus Cavite')
	 time.sleep(1)

	 btnSubmit = self.browser.find_element_by_id('btnSubmit')
	 btnSubmit.click()
	 time.sleep(2)


	 inputbground = self.browser.find_element_by_id("bground")
	 self.assertEqual(inputbground.get_attribute('placeholder'),'Background')
	 inputbground.click()
	 time.sleep(1)
	 inputbground.send_keys('add details on company history etc.')
	 time.sleep(1)

	 inputcapa = self.browser.find_element_by_id('capa')
	 self.assertEqual(inputcapa.get_attribute('placeholder'),'Capabilities')
	 inputcapa.click()
	 time.sleep(1)
	 inputcapa.send_keys('Milestone achieved')
	 time.sleep(1)


	 inputaccr = self.browser.find_element_by_id('accr')
	 self.assertEqual(inputaccr.get_attribute('placeholder'),'Accreditations')
	 inputaccr.click()
	 time.sleep(1)
	 inputaccr.send_keys('List of main Accreditation')
	 time.sleep(1)

	 inputstake = self.browser.find_element_by_id('stake')
	 self.assertEqual(inputstake.get_attribute('placeholder'),'Stakeholders')
	 inputstake.click()
	 time.sleep(1)
	 inputstake.send_keys('key shareholder')
	 time.sleep(1)

	 inputjobt = self.browser.find_element_by_id('jobt')
	 self.assertEqual(inputjobt.get_attribute('placeholder'),'Job title')
	 inputjobt.click()
	 time.sleep(1)
	 inputjobt.send_keys('Insert job title')
	 time.sleep(1)

	 inputjobv = self.browser.find_element_by_id('jobv')
	 self.assertEqual(inputjobv.get_attribute('placeholder'),'Job vacancy')
	 inputjobv.click()
	 time.sleep(1)
	 inputjobv.send_keys('20')
	 time.sleep(1)

	 inputjobsk = self.browser.find_element_by_id('jobsk')
	 self.assertEqual(inputjobsk.get_attribute('placeholder'),'Job skills and qualifications')
	 inputjobsk.click()
	 time.sleep(1)
	 inputjobsk.send_keys('required')
	 time.sleep(1)

	 inputposi = self.browser.find_element_by_id('posi')
	 self.assertEqual(inputposi.get_attribute('placeholder'),'Position')
	 inputposi.click()
	 time.sleep(1)
	 inputposi.send_keys('Manager')
	 time.sleep(1)

	 inputjobr = self.browser.find_element_by_id('jobr')
	 self.assertEqual(inputjobr.get_attribute('placeholder'),'Job responsibilities')
	 inputjobr.click()
	 time.sleep(1)
	 inputjobr.send_keys('Manage general')
	 time.sleep(1)

	 inputjobs = self.browser.find_element_by_id('jobs')
	 self.assertEqual(inputjobs.get_attribute('placeholder'),'Job salary')
	 inputjobs.click()
	 time.sleep(1)
	 inputjobs.send_keys('18,000')
	 time.sleep(1)

	 inputbene = self.browser.find_element_by_id('bene')
	 self.assertEqual(inputbene.get_attribute('placeholder'),'Benefits')
	 inputbene.click()
	 time.sleep(1)
	 inputbene.send_keys('life insurance')
	 time.sleep(1)

	 inputresu = self.browser.find_element_by_id('resu')
	 self.assertEqual(inputresu.get_attribute('placeholder'),'Resume')
	 inputresu.click()
	 time.sleep(1)
	 inputresu.send_keys('personalinformation')
	 time.sleep(1)

	 inputexam = self.browser.find_element_by_id('exam')
	 self.assertEqual(inputexam.get_attribute('placeholder'),'Examination')
	 inputexam.click()
	 time.sleep(1)
	 inputexam.send_keys('result of exams')
	 time.sleep(1)

	 inputdat = self.browser.find_element_by_id('dat')
	 self.assertEqual(inputdat.get_attribute('placeholder'),'Date')
	 inputdat.click()
	 time.sleep(1)
	 inputdat.send_keys('date of applicant')
	 time.sleep(1)

	 inputrema = self.browser.find_element_by_id('rema')
	 self.assertEqual(inputrema.get_attribute('placeholder'),'Remarks')
	 inputrema.click()
	 time.sleep(1)
	 inputrema.send_keys('Performance')
	 time.sleep(1)

	 inputstat = self.browser.find_element_by_id('stat')
	 self.assertEqual(inputstat.get_attribute('placeholder'),'Status')
	 inputstat.click()
	 time.sleep(1)
	 inputstat.send_keys('on and off')
	 time.sleep(1)

	 btnSubmit = self.browser.find_element_by_id('btnSubmit')
	 btnSubmit.click()
	 time.sleep(2)

	

	





































#from selenium import webdriver
#import unittest
#from selenium.webdriver.common.keys import Keys
#import time

#class PageTest(unittest.TestCase):

	#def setUp(self):
	 # self.browser = webdriver.Firefox()
	 #self.browser.maximize_window()

	'''
	def test_start_list_and_retrieve_it(self):
	 self.browser.get('http://localhost:8000')
	 self.assertIn("Customer complaint Form",self.browser.title)'''

	'''def check_for_rows_in_list_table(self,row_text):
	 table = self.browser.find_element_by_id('listTable')
	 rows = table.find_element_by_tag_name('tr')
	 #self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
	 self.browser.get('http://localhost:8000/')
	 self.assertIn("Customer Complaint Form",self.browser.title)

	 headerText = self.browser.find_element_by_tag_name('h1').text
	 self.assertIn("Customer Complaint Form", headerText)
	 inputbox = self.browser.find_element_by_id('Cntct')
	 self.assertEqual(inputbox.get_attribute('placeholder'), "Enter your Contact Number")
	 #inputbox.click()
	# inputbox.send_keys('09286631600')
	 time.sleep(1)	

	 name = self.browser.find_element_by_id('Ln')
	 name.click()
	 time.sleep(1)
	 name.send_keys('Rosalyn Pingol')
	 time.sleep(1)

	 Address = self.browser.find_element_by_id('add')
	 Address.click()
	 time.sleep(1)
	 Address.send_keys('Blk 20 Lot 10 Imus')
	 time.sleep(1)

	 contact = self.browser.find_element_by_id('Cntct')
	 contact.click()
	 time.sleep(1)
	 contact.send_keys('091234567')
	 time.sleep(1)

	 email = self.browser.find_element_by_id('Eml')
	 email.click()
	 time.sleep(1)
	 email.send_keys('rosalyn@gmail.com')
	 time.sleep(1)

	 detailed = self.browser.find_element_by_id('Locincident')
	 detailed.click()
	 time.sleep(1)
	 detailed.send_keys('item')
	 time.sleep(1)

	 btnSubmit = self.browser.find_element_by_id('btnSubmit')
	 btnSubmit.click()
	 time.sleep(2)

	 contact = self.browser.find_element_by_id('Cntct')
	 contact.click()
	 time.sleep(1)
	 contact.send_keys('0948755621')
	 time.sleep(1)

	 email = self.browser.find_element_by_id('Eml')
	 email.click()
	 time.sleep(1)
	 email.send_keys('leonalyn@gmail.com')
	 time.sleep(1)

	 detailed = self.browser.find_element_by_id('Locincident')
	 detailed.click()
	 time.sleep(1)
	 detailed.send_keys('service')
	 time.sleep(1)
	 btnSubmit = self.browser.find_element_by_id('btnSubmit')
	 btnSubmit.click()
	 time.sleep(2)

	 #self.assertIn('1: 091234567 rosalyn@gmail.com complaint item', [row.text for row in rows])
	 #self.assertIn('1: 0948755621 leonalyn@gmail.com complaint service', [row.text for row in rows])


	 self.check_for_rows_in_list_table('1: 091234567 rosalyn@gmail.com complaint item')
	 self.check_for_rows_in_list_table("1: 0948755621 leonalyn@gmail.com complaint service")
	 table = self.browser.find_element_by_id('listTable')
	 rows = table.find_element_by_tag_name('tr')

if __name__=='__main__':
	unittest.main()
















	
	inputbox2 = self.browser.find_element_by_id('Eml')
	 self.assertEqual(inputbox2.get_attribute('placeholder'), "Enter your Email")
	 inputbox2.click()
	 inputbox2.send_keys('Rose.deniega@gmail.com')
	 time.sleep(1)	

	 inputbox3 = self.browser.find_element_by_id('Locincident')
	 self.assertEqual(inputbox3.get_attribute('placeholder'), "Detailed of your complaint")
	 inputbox3.click()
	 inputbox3.send_keys('Customer service')
	 time.sleep(1)


	 table = self.browser.find_element_by_id('listTable')
	 rows = table.find_element_by_tag_name('tr')

	 btnSubmit = self.browser.find_element_by_id('btnSubmit')
	 btnSubmit.click()'''







