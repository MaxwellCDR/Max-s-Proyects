from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from requests_html import HTMLSession

def main():
    url_fullha4rd = "https://www.gamingcity.com.ar/monitor-corsair-xeneon/p/MLA44659275?pdp_filters=seller_id%3A91988078#polycard_client=search-nordic-mshops&position=26&search_layout=grid&type=item&tracking_id=49635dec-7057-4f09-afbd-a358cd73d16f&wid=MLA1473046549&sid=search"
    session = HTMLSession()
    product_page = session.get(url_fullha4rd)

    # Area de testeo de clases
    found = product_page.html.find(".andes-button--quiet")
    print(found)

    if len(found) > 0:
        driver = webdriver.Firefox()  # Te conectas al driver que maneja FireFox
        driver.get(url_fullha4rd) # Obtenés acceso a la URL de GamingCity, porque tuve que cambiarla por motivos prácticos

        # Revisar los medios de pago y regresar a la pagina anterior
        driver.find_element(By.CSS_SELECTOR, ".ui-pdp-price__payments-link").click() # Va a hacer click en los diferentes medios de pago disponibles que encuentre
        driver.back() # Va a regresar a la pestaña anterior

        # Agregar al carrito
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, ":r1:"))).click()

        # Aceptar las cookies
        driver.find_element(By.CLASS_NAME, "nav-cookie-disclaimer__button").click()

        # Cerrar la zona de checkout provisoria
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".andes-modal__close-button"))).click()

        # Ir directo a la zona de check out
        driver.find_element(By.ID, "nav-cart").click()

        # Cierre del navegador
        driver.quit()

if __name__ == "__main__":
    main()

# Comentarios por linea (In-Line Comments)

# Línea 25: basicamente va a identificar por ID el boton de agregar al carrito y va a agregar el item al carrito
# Algo que se debe tener en cuenta es que se ha usado WebDriverWait, en caso de que el elemento tarde en cargarse, de ese modo, no va a haber un error por elemento no encontrado
# Se ha usado Expected Conditions (EC) para justamente aguardar a que el elemento este listo para clickearlo

# Línea 28: encuentra el boton de las cookies mediante clase y acepta las cookies de la web

# Linea 31: para poder ir al carrito hayq ue hacerlo de modo manual, y para hacer eso hay que salir de la prevista del carrito de compras, e ir al carrito en la web principal, asique mediante selector se cierra la ventana provisoria para ir a la página principal y clickear el carrito

# Linea 34: mediante ID buscamos el icono de carrito, le damos click y nos vamos a la zona de checkout



# Clase de respaldo: ui-pdp-container