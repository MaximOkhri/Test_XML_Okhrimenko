import requests
import bs4
from bs4 import BeautifulSoup
from lxml import etree
import datetime

class CheckingMethods():

    def check_data_type():  

        result = requests.get('https://www.cbr.ru/StaticHtml/File/92172/ValCurs.xsd')
        content = result.content

        numeric_type_names = []
        soup = BeautifulSoup(content, 'xml')

        elements = soup.find_all('element', type='xs:unsignedShort')
        for element in elements:
            numeric_type_names.append(element['name'])

        elements = soup.find_all('element', type='xs:unsignedInt')
        for element in elements:
            numeric_type_names.append(element['name'])

        result = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002')
        content = result.content

        soup = BeautifulSoup(content, 'xml')

        for el in soup.find_all(numeric_type_names):
            try:    
                tmp = int(el.text)
            except ValueError:
                assert False, 'Cannot change data type to integer'

    def check_xml_currency_ids():

        xml_currency_ids = []
        xml_main_file = etree.parse('ValCursFile.xml')
        id_codes = xml_main_file.findall('Valute')
        for id_code in id_codes:
            id = id_code.get('ID')
            xml_currency_ids.append(id)

        url_code_xml = 'https://www.cbr.ru/scripts/XML_val.asp?d=0'

        response = requests.get(url_code_xml)
        f = open('ValuteCode.xml', 'wb+')
        f.write(response.content)
        f.close()

        currency_ids = []
        xml_code_file = etree.parse('ValuteCode.xml')
        id_items = xml_code_file.findall('Item')
        for id_item in id_items:
            id = id_item.get('ID')
            currency_ids.append(id)

        xml_currency_ids_is_valid = True

        for i in xml_currency_ids:
            if i not in currency_ids:
                xml_currency_ids_is_valid = False

        assert xml_currency_ids_is_valid == True, 'xml currency ids is not valid'

    def check_xml_date():
        
        attributes = {}
        tree = etree.parse('CurrentDateFile.xml')
        root = tree.getroot()
        for elem in root.iter():
            attributes.update(elem.attrib)

        xml_date = attributes['Date']
        
        check_xml_date = str(xml_date)

        current_date = str(datetime.datetime.now().strftime("%d.%m.%Y"))

        assert current_date == check_xml_date, 'The file date does not match the current one'