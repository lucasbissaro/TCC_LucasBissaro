from selenium import webdriver
import sys
import time
#https://pt.pornhub.com/view_video.php?viewkey=ph5a0da36f9671e

try:
	ini = time.time()
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument("--mute-audio")
	options.add_argument('--disable-gpu')
    #options.add_argument('window-size=1200x600')

	driver = webdriver.Chrome(chrome_options=options)
	print ( time.time() - ini)
	#driver.set_window_size(1120, 550)
	link = sys.argv[1]
	driver.get(link)
	test = driver.find_element_by_tag_name("polygon").get_attribute('points').split(" ")
	coordenadas = [x.split(",") for x in test]

	#print(coordenadas)

	print ( time.time() - ini)
	driver.quit()
	print ( time.time() - ini)


    
except:
    driver.quit()