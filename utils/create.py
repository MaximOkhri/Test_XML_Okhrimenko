import requests 

class CreateFiles():

    def create_xml_file():

        url_xml = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002'

        response = requests.get(url_xml)
        f = open('ValCursFile.xml', 'wb+')
        f.write(response.content)
        f.close()

    def create_xml_file_with_current_date():

        url_xml = 'https://www.cbr.ru/scripts/XML_daily.asp'

        response = requests.get(url_xml)
        f = open('CurrentDateFile.xml', 'wb+')
        f.write(response.content)
        f.close()

    def create_xsd_file():

        url_xsd = 'https://www.cbr.ru/StaticHtml/File/92172/ValCurs.xsd'

        response = requests.get(url_xsd)
        f = open('Shema.xsd', 'wb+')
        f.write(response.content)
        f.close()