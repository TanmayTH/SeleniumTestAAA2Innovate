# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 23:00:46 2021

@author: TANMAY HARSH
"""


import os
import csv
import unittest
import HtmlTestRunner
import platform
from time import sleep
from parameterized import parameterized_class
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


if platform.system()=='Windows':
    ROOT_PATH='/'.join(__file__.split("\\")[:-2])+'/' #conc
else: ROOT_PATH='/'.join(__file__.split("/")[:-2])+'/'

TEST_DATA_CSV_PATH=ROOT_PATH+"TestDataCSV/"
DRIVER_PATH=ROOT_PATH+"Driver/"


#Getting all tests' values and parameters:
with open(TEST_DATA_CSV_PATH+os.listdir(TEST_DATA_CSV_PATH)[0]) as csvdic:
    reader=csv.DictReader(csvdic)
    test_variables=reader.fieldnames
    test_variable_values_list=[tuple(i.values()) for i in reader]



@parameterized_class(test_variables, test_variable_values_list)
class TESTING__erpcustomer_zipaworld_com_Home(unittest.TestCase):  
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(executable_path=DRIVER_PATH+os.listdir(DRIVER_PATH)[0])
        self.driver.get("http://deverpcustomer.zipaworld.com/")
        self.driver.implicitly_wait(1)

    
    def test_1__Ocean_ByDefault_in_ModalityOfTRansport(self):
        self.is_ocean=self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]").text
        self.ocean_active=self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]").get_attribute('class')
        if 'active' not in self.ocean_active:
            self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
        
        assert 'active' in self.ocean_active and 'Ocean'==self.is_ocean, "Ocean Bar is Not Selected by default"
    
    

    def test_2__General_byDefault_in_commodityToBeTranspoRTed(self):
        self.general_byDefault=self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").get_attribute('class')
        self.is_general=self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").text
        if 'active' not in self.general_byDefault:
            self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        
        assert 'active' in self.general_byDefault and 'General'==self.is_general, "'General' Not selected ByDefault in 'Commodity to be transported'"
        
    
    
    def test_3__ByDefault_OriginPort2DestinationPort_under_GeneralCommodity(self):
        self.is_OriginPort2DestinationPort=self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]").text
        self.is_SelectedByDefault=self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]").get_attribute('checked')
        if not self.is_SelectedByDefault:
            self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        
        assert self.is_OriginPort2DestinationPort=='Origin Port To Destination Port' and self.is_SelectedByDefault,"'Origin Port To Destination Port' Not selected ByDefault"
    


    def test_4__Fill_originPort2DestinationPort_form(self):
        self.driver.execute_script("window.scrollBy(0,300)")
        ##Clicking 'from and to' form:-
        self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/label[1]").click()
        #Entering origin port and destination port:
        AC(self.driver).move_to_element(self.driver.find_element_by_xpath("//div[contains(text(),'Search Your Origin Port')]")).click().send_keys(self.ORIGIN).pause(1).send_keys(Keys.ENTER).perform()
        AC(self.driver).move_to_element(self.driver.find_element_by_xpath("//div[contains(text(),'Search Your Destination Port')]")).click().send_keys(self.DESTINATION).pause(1).send_keys(Keys.ENTER).perform()
    
    

    def test_5__Filling_shipmentMode(self):
        ##working with shipment mode:-
        #Container type:
        def Container_Type_Handler(self):
            for _ in range(int(self.STD20)): self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[3]/i[1]").click()
            for _ in range(int(self.STD40)): self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[3]/i[1]").click()
            for _ in range(int(self.HC40)): self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[1]/div[2]/div[3]/ul[1]/li[3]/i[1]").click()
        
        self.is_FCL_container_byDefault=self.driver.find_element_by_xpath("//div[contains(text(),'FCL')]").text
        if self.is_FCL_container_byDefault!='FCL':
            self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]").click()
            self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[1]/div[1]/div[2]").click()
            Container_Type_Handler(self)
        else:
            self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]").click()
            Container_Type_Handler(self)



    def test_6__Filling_Commodity_HSN(self):
        #Filling Commodity HSN:-
        self.commodity_num=3011100  #provided
        self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[6]/div[1]").click()
        AC(self.driver).move_to_element(self.driver.find_element_by_xpath("//div[contains(text(),'Search Commodity')]")).click().send_keys(self.commodity_num).pause(1).send_keys(Keys.ENTER).perform()


    
    def test_7__PackageDetails_Form_Filling__and__LBS_to_KG_Accuracy(self):
        self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[5]").click()
        WebDriverWait(self.driver,5,0.7).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="grossWeightLbs"]')))
        #Entering LBS gross wt:
        self.driver.find_element_by_css_selector('input[name="grossWeightLbs"]').send_keys(int(self.GROSS_WT_LBS))
        #Getting KG gross wt by website:
        self.GrossWT_KG=float(self.driver.find_element_by_css_selector('input[name="grossWeight"]').get_attribute('value'))

        #Filling Total pieces and volume weight:
        self.driver.find_element_by_css_selector('input[name="totalPieces"]').send_keys(int(self.TOTAL_PIECES))
        self.driver.find_element_by_css_selector('input[name="volumeWeight"]').send_keys(int(self.VOLUME))

        def LBS_to_KG(lbswt):
            return round(0.45359237*lbswt, 2)
        
        self.WT_conversiom_Error_msg=f"""Problem With Weight Conversion from 'LBS' to 'KG'
        Wrong result for '{int(self.GROSS_WT_LBS)} LBS': Expected '{LBS_to_KG(int(self.GROSS_WT_LBS))} KG', Found '{self.GrossWT_KG} KG'
        """
        assert self.GrossWT_KG==LBS_to_KG(int(self.GROSS_WT_LBS)), self.WT_conversiom_Error_msg

        self.driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
    


    def test_8__Prices_Validation(self):
        #Provided Conversion Rates:-
        self.USD1_to_EUR=0.84
        self.EUR1_to_USD=1.19
        
        self.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[4]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]").click()
        self.driver.switch_to_alert().accept()
        sleep(0.8)
        self.driver.find_element_by_css_selector('button[aria-label="Close"]').click()
        sleep(.6)
        self.driver.find_element_by_link_text("Freight Summary").click()

        #details of different type of containers displayed:-
        self.NumContainer20=int(self.driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tr[2]/td[1]").text)
        self.NumContainer40=int(self.driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tr[3]/td[1]").text)
        self.NumContainer40HC=int(self.driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tr[4]/td[1]").text)
        self.item20Price_per_commodity_inUSD=float(self.driver.find_element_by_css_selector("body.ltr:nth-child(2) div.h-100 div.menu-hidden div.dashboard-wrapper.padding-bottomss1 div.container-fluid div.row div.col-lg-12.padding-leftright div.express_card:nth-child(3) div.container div.flights-types1.our_card div.rate-card.mb-3 div.collapse.border-top.show:nth-child(4) div.d-flex.flex-wrap.justify-content-between.padding-15 div.all-price.list-fare table.table.pricess-all tr:nth-child(2) > td:nth-child(3)").text.split()[1])
        self.item40Price_per_commodity_inUSD=float(self.driver.find_element_by_css_selector("body.ltr:nth-child(2) div.h-100 div.menu-hidden div.dashboard-wrapper.padding-bottomss1 div.container-fluid div.row div.col-lg-12.padding-leftright div.express_card:nth-child(3) div.container div.flights-types1.our_card div.rate-card.mb-3 div.collapse.border-top.show:nth-child(4) div.d-flex.flex-wrap.justify-content-between.padding-15 div.all-price.list-fare table.table.pricess-all tr:nth-child(3) > td:nth-child(3)").text.split()[1])
        self.item40HCPrice_per_commodity_inUSD=float(self.driver.find_element_by_css_selector("body.ltr:nth-child(2) div.h-100 div.menu-hidden div.dashboard-wrapper.padding-bottomss1 div.container-fluid div.row div.col-lg-12.padding-leftright div.express_card:nth-child(3) div.container div.flights-types1.our_card div.rate-card.mb-3 div.collapse.border-top.show:nth-child(4) div.d-flex.flex-wrap.justify-content-between.padding-15 div.all-price.list-fare table.table.pricess-all tr:nth-child(4) > td:nth-child(3)").text.split()[1])
        self.item20Price_eur=float(self.driver.find_element_by_css_selector("body.ltr:nth-child(2) div.h-100 div.menu-hidden div.dashboard-wrapper.padding-bottomss1 div.container-fluid div.row div.col-lg-12.padding-leftright div.express_card:nth-child(3) div.container div.flights-types1.our_card div.rate-card.mb-3 div.collapse.border-top.show:nth-child(4) div.d-flex.flex-wrap.justify-content-between.padding-15 div.all-price.list-fare table.table.pricess-all tr:nth-child(2) > td:nth-child(4)").text.split()[1])
        self.item40Price_eur=float(self.driver.find_element_by_css_selector("body.ltr:nth-child(2) div.h-100 div.menu-hidden div.dashboard-wrapper.padding-bottomss1 div.container-fluid div.row div.col-lg-12.padding-leftright div.express_card:nth-child(3) div.container div.flights-types1.our_card div.rate-card.mb-3 div.collapse.border-top.show:nth-child(4) div.d-flex.flex-wrap.justify-content-between.padding-15 div.all-price.list-fare table.table.pricess-all tr:nth-child(3) > td:nth-child(4)").text.split()[1])
        self.item40HCPrice_eur=float(self.driver.find_element_by_css_selector("body.ltr:nth-child(2) div.h-100 div.menu-hidden div.dashboard-wrapper.padding-bottomss1 div.container-fluid div.row div.col-lg-12.padding-leftright div.express_card:nth-child(3) div.container div.flights-types1.our_card div.rate-card.mb-3 div.collapse.border-top.show:nth-child(4) div.d-flex.flex-wrap.justify-content-between.padding-15 div.all-price.list-fare table.table.pricess-all tr:nth-child(4) > td:nth-child(4)").text.split()[1])
        
        def EuroPriceCalculator(items, usd_price_per_item):
            return items*usd_price_per_item*0.84
        
        def ErrorMsgFormatter(items, usd_price_per_item, Expected_euro, found_euro):
            return f'''Error in "USD to EURO" Accuracy !
            For Number of items: "{items}", Price per item in USD: "{usd_price_per_item}"
            EXPECTED Price in Euro: "{Expected_euro}", FOUND Price in Euro: "{found_euro}"
            '''
        
        assert self.item20Price_eur==EuroPriceCalculator(self.NumContainer20, self.item20Price_per_commodity_inUSD), ErrorMsgFormatter(self.NumContainer20, self.item20Price_per_commodity_inUSD, EuroPriceCalculator(self.NumContainer20, self.item20Price_per_commodity_inUSD), self.item20Price_eur)
        assert self.item40Price_eur==EuroPriceCalculator(self.NumContainer40, self.item40Price_per_commodity_inUSD), ErrorMsgFormatter(self.NumContainer40, self.item40Price_per_commodity_inUSD, EuroPriceCalculator(self.NumContainer40, self.item40Price_per_commodity_inUSD), self.item40Price_eur)
        assert self.item40HCPrice_eur==EuroPriceCalculator(self.NumContainer40HC, self.item40HCPrice_per_commodity_inUSD), ErrorMsgFormatter(self.NumContainer40HC, self.item40HCPrice_per_commodity_inUSD, EuroPriceCalculator(self.NumContainer40HC, self.item40HCPrice_per_commodity_inUSD), self.item40HCPrice_eur)


    @classmethod
    def tearDownClass(self):
        self.driver.quit()

  
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=ROOT_PATH+"HTML_RepoRTs/"))
