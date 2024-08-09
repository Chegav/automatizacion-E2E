# Automatizacion E2E  

COMO LO EJECUTAMOS  

# Guía para Ejecutar la Prueba E2E en Sauce Demo

## Requisitos Previos

1. **Instalar Python**:
   - Asegúrate de tener Python 3.6 o superior instalado en mi sistema.
   - Lo descargo desde [python.org](https://www.python.org/downloads/).

2. **Instalar ChromeDriver**:
   - Asegúrate de tener ChromeDriver compatible con la versión de Google Chrome que tengo.
   - Lo descargo desde [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).

3. **Instalar PyCharm**:
   - PyCharm es el IDE que utilizo para programar en Python.
   - Lo descargo desde [JetBrains PyCharm](https://www.jetbrains.com/pycharm/download/).

## Pasos para Ejecutar la Prueba

1. **Clonar el Repositorio**:
   - Abro una terminal o línea de comandos.
   - Ejecuto el siguiente comando para clonar el repositorio desde GitHub:
     ```bash
     git clone https://github.com/Chegav/ApiTest.git
     ```

2. **Navegar al Directorio del Proyecto**:
   - Cambio al directorio del proyecto clonado:
     ```bash
     cd ApiTest
     ```

3. **Instalar las Dependencias**:
   - Me aseguro de que `pip` esté instalado.
   - Ejecuto el siguiente comando para instalar las dependencias necesarias:
     ```bash
     pip install selenium
     ```

4. **Configurar el Entorno en PyCharm**:
   - Abro PyCharm y elijo "Open" para abrir el directorio del proyecto clonado.
   - PyCharm detectará automáticamente el archivo `requirements.txt` (si existe) y me pedirá instalar las dependencias.

5. **Agregar ChromeDriver al PATH**:
   - Me aseguro de que el archivo `chromedriver` esté en mi PATH.
   - O bien, coloco el archivo `chromedriver` en el mismo directorio donde se encuentra mi script Python.

6. **Ejecutar el Script de Prueba**:
   - En PyCharm, abro el archivo `test.py`.
   - Hago clic en el botón de "Run" en la esquina superior derecha o uso el atajo de teclado `Shift + F10`.

## Descripción del Script

- **Inicio del Navegador**:
  - Abro la página `https://www.saucedemo.com/`.

- **Inicio de Sesión**:
  - Ingreso las credenciales `standard_user` y `secret_sauce`.

- **Agregar Productos al Carrito**:
  - Selecciono dos productos al azar y los agrego al carrito.

- **Visualizar el Carrito y Completar Compra**:
  - Accedo al carrito, completo el formulario de compra, y finalizo la compra.

- **Confirmación**:
  - Verifico que el mensaje de confirmación sea "Thank you for your order!".

## Notas

- Me aseguro de que el navegador y ChromeDriver sean compatibles.
- Puedo ajustar los tiempos de espera (`time.sleep()`) según la velocidad de mi conexión a Internet y la carga del sitio web.

Para cualquier duda o problema, reviso la documentación de Selenium o consulto los foros de soporte.
