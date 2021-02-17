# challenge
Cumplo Challenge

Ésta aplicación web que permite obtener el valor de la UDIS y el dólar cumpliendo con las siguientes condiciones:
- Definir el rango de tiempo (fecha inicial y fecha final) a consultar.
- La información debe ser consumida desde el web service oficial de Banxico
https://www.banxico.org.mx/SieAPIRest/service/v1/;jsessionid=5fa4f900baccc38cd60cb4f38981
- El sistema debe responder desplegando los siguientes datos:
  * Los valores en pesos de las UDIS para cada día para el rango definido
  * El promedio, valor máximo y mínimo de las UDIS para el rango definido
  * Un gráfico que despliegue los valores de las UDIS para cada día para el
  rango definido
  * Los valores en pesos del dólar para cada día para el rango definido
  * El promedio, valor máximo y mínimo del dólar para el rango definido
  * Un gráfico que despliegue los valores del dólar para cada día para el rango
  definido

Se requiere además otro dato financiero, la TIIE (Tasas de Interés Interbancarias):
El sistema debe responder desplegando los siguientes datos:
- Visualizar la TIIE para los distintos tipos de plazos y montos de créditos
- Poder visualizar el histórico en un gráfico y que se destaque el más alto por
tipo.

Referencia Banxico:
https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?sector=18&accion=consultarCuadro&idCuadro=CF111&locale=es

Glosario:
UDI’s = https://contadorcontado.com/2015/10/12/que-son-las-udis-y-para-que-sirven/
TIIE = https://tiie.com.mx/tasa-tiie/

Las herramientas necesarias son las siguientes:
- python 3.6
- Django:   pip install django
- Requests: pip install requests
- Json:     pip install jason

Clonar el repositorio en una carpeta local, posteriormente desde una terminal o consola 
dirigirse a la carpeta del proyecto, ubicar el script manage.py y ejecutar el comando
python manage.py runserver

Acceder a la dirección http://127.0.0.1:8000/ para poder ejecutar la aplicación web.
