import requests
from bs4 import BeautifulSoup
import csv

def scrape_jobs():
    # Usamos una página de pruebas (quotes.toscrape.com) para no violar términos de servicio
    url = "http://quotes.toscrape.com/"
    print(f"🔍 Conectando a {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Lanza error si la página falla
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscamos las frases y autores
        quotes = soup.find_all('div', class_='quote')
        
        datos = []
        for quote in quotes:
            texto = quote.find('span', class_='text').text
            autor = quote.find('small', class_='author').text
            datos.append({"texto": texto, "autor": autor})
            
        print(f"✅ Se encontraron {len(datos)} registros.")
        
        # Guardar en CSV
        with open('datos_extraidos.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["texto", "autor"])
            writer.writeheader()
            writer.writerows(datos)
            
        print("💾 Datos guardados en 'datos_extraidos.csv'")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    scrape_jobs()