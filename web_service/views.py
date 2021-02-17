"""
@author: Jorge Salazar
@since: 14 Feb 2021
@TODO: This script request information from Banxico web service
       to get the UDIS and Dollar value requested from a time
        period and shows with the following requirements.

        UDIS
        - Print the UDIS's value in Pesos foreach day of the
        defined time period.
        - Print the average, max value and min value of the UDIS in
        the time period.
        - Draw a graph with the UDIS's values by the days in the
        time period.

        DOLLAR
        - Print the Dollar's value in Pesos foreach day of the
        defined time period.
        - Print the average, max value and min value of the Dollar in
        the time period.
        - Draw a graph with the Dollar's values by the days in the
        time period.
"""

from django.shortcuts import get_object_or_404, render
import requests
import json


class RequestUtil:

    def __init__(self):
        self.url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/'
        self.headers = {
            'Bmx-Token': 'd7c3482635131008a0bd73ef4aaa1bdfcfdebeccee800c932175434a5c52ed9a'
        }


    def build_url(self, idSerie, fechaIni=None, fechaFin=None):
        """
        This funciton builds the url to sent request
        :param idSerie: the Id of the Banxico catalog
        :type idSerie: str
        :param fechaIni: The period start to consult in format YYYY-MM-DD
        :type fechaIni: str
        :param fechaFin: The period end to consult in format YYYY-MM-DD
        :type fechaFin: str
        :returns: The built url to send to requests function
        :rtype: str
        """
        if (fechaIni or fechaFin) and not(fechaIni == '' or fechaFin == ''):
            params = '%s/datos/%s/%s' % (''.join(idSerie), fechaIni, fechaFin)
        else:
            raise AttributeError("Please insert a valid time period")
        print(self.url + params)
        return self.url + params



    def send_request(self, url):
        """
        This function send a request to HTTP server.
        :param url: the built url to request data
        :type url: str
        :param headers: the headers of the request
        :type headers: str
        :returns: the content of the request
        :rtype: str
        """
        response    = requests.get(url, headers=self.headers)
        status_code = response.status_code

        if response.status_code == 200:
            content = response.content
            return content
        raise ValueError('The request finished with code %s' % status_code)


    def parse_content(self, content):
        """
        This function parses the request content into a dictionary structure
        to show the data in the templates.
        :param content: the returned request content
        :type content: json
        :returns: Data structured into a dictionary
        :rtype: dictionary
        """
        content = json.loads(content)
        parsed_content_list = []

        for serie in content['bmx']['series']:
            parsed_content = {}
            parsed_content['title'] = serie['titulo']
            parsed_content['data'] = serie['datos']

            data = [float(dato['dato']) for dato in serie['datos']]

            parsed_content['average'] = round(sum(data) / len(data), 6)
            parsed_content['min'] = min(data)
            parsed_content['max'] = max(data)

            parsed_content_list.append(parsed_content)

        return parsed_content_list


###
# Views functions to render templates
###
def home(request):
    """
    This function builds the index page using the index.html template
    from web_service django application.
    """
    request_content = None
    error_message = None
    if request.method == 'POST':
        # Request data to Banxico web service
        banx_req_obj = RequestUtil()
        try:
            request_url = banx_req_obj.build_url(
                request.POST['idSerie'],
                request.POST['fechaIni'],
                request.POST['fechaFin']
            )
            request_content = banx_req_obj.send_request(request_url)
            request_content = banx_req_obj.parse_content(request_content)
        except Exception as e:
            error_message = str(e)
    context = {
        'content_list': request_content,
        'error_message': error_message,
    }
    return render(request, 'web_service/index.html', context)
