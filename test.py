from splinter import Browser

import matplotlib.pyplot as plt
import sys
with Browser("phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any']) as browser:
    # Optional, but make sure large enough that responsive pages don't
    # hide elements on you...
    browser.driver.set_window_size(1280, 1024)
    # Open the page you want...
    browser.visit('https://www.google.com.br')
    print(browser.html)
    print(browser.url)
    '''
    test = browser.find_by_tag("polygon")#.get_attribute('points').split(" ")
    coordenadas = [x.split(",") for x in test]

	#print(coordenadas)
	#separa os a coluna de x e y para plotar
    coluna0 = [x[0] for x in coordenadas]
    coluna1 = [100-int(x[1]) for x in coordenadas]'''
    #browser.driver.save_screenshot('picture.png')
	#fecha o driver
    #driver.quit()
    #print(test)
	#plota o grafico
    #plt.plot(coluna0, coluna1)
    #plt.fill_between(coluna0, 0, coluna1)
    #plt.show()
    # submit the search form...
    '''browser.fill("q", "parliament")
    button = browser.find_by_css("button[type='submit']")
    button.click()
    # Scrape the data you like...
    links = browser.find_by_css(".search-results .list-group-item")
    for link in links:
        print (link['href'])'''