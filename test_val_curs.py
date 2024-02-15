import pytest
from utils.validator import ValidateMethod
from utils.create import CreateFiles
from utils.checking import CheckingMethods

@pytest.mark.xmltest
class TestValCurs():

    @pytest.mark.validate
    def test_validate(self):

        CreateFiles.create_xml_file()
        CreateFiles.create_xsd_file()
        ValidateMethod.validate_xml_file('ValCursFile.xml',  'Shema.xsd')

    @pytest.mark.check
    def test_check_xml_currency_ids(self):

        CreateFiles.create_xml_file()
        CheckingMethods.check_xml_currency_ids()

    @pytest.mark.check
    def test_check_type_data(self):

        CheckingMethods.check_data_type()
    
    @pytest.mark.check
    def test_xml_date(self):

        CreateFiles.create_xml_file_with_current_date()
        CheckingMethods.check_xml_date()



    