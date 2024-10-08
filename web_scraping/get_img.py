import requests
import bs4

resultado = requests.get('https://escueladirecta.com/')
soup = bs4.BeautifulSoup(resultado.text, 'lxml')

# Select the src content of an employees element from soup
images = soup.select('.course-box-image')[0]['src']
# Get the employees written in binary
img_bi = requests.get(images).content

# Create a jpg file and write in binary the employees
file = open('my_image.jpg', 'wb')
file.write(img_bi)
file.close()