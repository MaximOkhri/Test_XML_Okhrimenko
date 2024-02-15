from lxml import etree

class ValidateMethod():

    def validate_xml_file(xml_path: str, xsd_path: str):

        try: 
            xsd_root = etree.parse(xsd_path)
            xmlschema = etree.XMLSchema(xsd_root)

            xml_doc = etree.parse(xml_path)
            if not xmlschema.validate(xml_doc):
                print(xmlschema.error_log)
            else:
                print('Valid')
        except etree.XMLSyntaxError:
            assert False, 'File is not xml-file'

        assert xmlschema.validate(xml_doc) == True, 'File have a mistake'

    