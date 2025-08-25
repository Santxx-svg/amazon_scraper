import requests
from bs4 import BeautifulSoup
import csv

url_base = "https://www.amazon.com/s?k=gaming&language=es&_encoding=UTF8&content-id=amzn1.sym.edf433e2-b6d4-408e-986d-75239a5ced10&pd_rd_r=bf0626fd-6c56-4395-8749-d448f3bc7f64&pd_rd_w=EGdh6&pd_rd_wg=BUjYH&pf_rd_p=edf433e2-b6d4-408e-986d-75239a5ced10&pf_rd_r=ASJXAK1A4MRPWQP4A6M7&ref=pd_hp_d_atf_unk"

headers = {

    'User-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

respuesta = requests.get(url_base, headers = headers)
contenido_html = respuesta.text

soup = BeautifulSoup(contenido_html, 'html.parser')

contenedores_productos = soup.find_all('div', {'data-cy': 'title-recipe'})

datos = []

for producto in contenedores_productos:
    try:

        titulo = producto.find('h2').text

        precio = producto.find('span', class_='a-offscreen').text

        datos.append({'titulo': titulo, 'precio': precio})
    except AttributeError:
        continue

with open('productos_gaming.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    encabezados = ['titulo', 'precio']
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados)

    escritor_csv.writeheader()
    escritor_csv.writerows(datos)

print("Los datos se guardaron.")
