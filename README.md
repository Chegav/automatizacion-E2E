# Automatizacion E2E  

## Requisitos Previos

1. **Instalar Python**:
-Nos aseguramos de tener Python 3.6 o superior instalado en mi sistema.
-O lo descargamos desde [python.org](https://www.python.org/downloads/).

2. **Instalar ChromeDriver**:  
-En este caso ChromeDriver ya viene por defecto en Chrome solo debemos instalar Google Chrome

4. **Instalar PyCharm**:  
-Lo descaramoso desde [JetBrains PyCharm](https://www.jetbrains.com/pycharm/download/).

## Pasos para Ejecutar la Prueba

1. **Clonar el Repositorio**:    
-Abro una terminal o línea de comandos.  
-Ejecuto el siguiente comando para clonar el repositorio desde GitHub:
     ```bash
     git clone https://github.com/Chegav/ApiTest.git
     ```

2. **Navegar al Directorio del Proyecto**:  
-Cambio al directorio del proyecto clonado:
     ```bash
     cd ApiTest
     ```

3. **Instalar las Dependencias**:  
-Me aseguro de que `pip` esté instalado.  
-Ejecuto el siguiente comando para instalar las dependencias necesarias:
     ```bash
     pip install selenium
     ```

4. **Configurar el Entorno en PyCharm**:  
-Abro PyCharm y elijo "Open" para abrir el directorio del proyecto clonado.  
-PyCharm detectará automáticamente el archivo `requirements.txt` (si existe) y me pedirá instalar las dependencias.  

5. **Ejecutar el Script de Prueba**:  
-En PyCharm, abro el archivo `test.py`.  
-Hago clic en el botón de "Run" en la esquina superior derecha o uso el atajo de teclado `Shift + F10`.
