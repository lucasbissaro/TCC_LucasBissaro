from selenium import webdriver
import matplotlib.pyplot as plt
import sys

#https://pt.pornhub.com/view_video.php?viewkey=ph5a0da36f9671e

try:
	options = webdriver.ChromeOptions()

	#desativa som, tira a interface.
	options.add_argument('headless')
	options.add_argument("--mute-audio")
	options.add_argument('window-size=1200x600')

	# initialize the driver
	driver = webdriver.Chrome(chrome_options=options)

	driver.set_window_size(1120, 550)
	#pega o link e abre no navegador
	link = sys.argv[1]
	driver.get(link)
	#acha o elemento de tag polygon e pega o atributo points() e separa pelo ' ' para vir em um vetor com cada par [x,y]
	test = driver.find_element_by_tag_name("polygon").get_attribute('points').split(" ")
	#separa o x do y, eles vem em uma string separada por ',', mas ainda sim é um elemento só.
	coordenadas = [x.split(",") for x in test]

	#print(coordenadas)
	#separa os a coluna de x e y para plotar
	coluna0 = [x[0] for x in coordenadas]
	coluna1 = [100-int(x[1]) for x in coordenadas]

	#fecha o driver
	driver.quit()

	#plota o grafico
	plt.plot(coluna0, coluna1)
	plt.fill_between(coluna0, 0, coluna1)
	plt.show()

    
except:
    driver.quit()