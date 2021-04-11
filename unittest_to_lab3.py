import unittest
from models.insurance_type_list import InsuranceType
from models.property_list import Property
from models.benefits_list import Benefits
from models.corporate_list import CorporateInsurancesType
from manager.insurance_mang import InsuranceManager
from models.types_insure import PropertyInsurance, LifeInsurance, CorporateInsurance
from models.sort_order import SortOrder


class TestInsurance(unittest.TestCase):

    def setUp(self):
        self.obj1 = PropertyInsurance(Property.HOUSE, 500000, 180000, 'Insure Housing', InsuranceType.PROPERTY, 24,
                                      10000, 15, ['fire', 'robbery', 'tornado', 'burglary', 'flood'])
        self.obj2 = LifeInsurance('John Jonson', 'Jack Billin', [Benefits.JURIDICAL_HELP], 'VSCU Safety',
                                  InsuranceType.LIFE, 36, 15500, 12, ['deaths', 'car accident'])
        self.obj3 = CorporateInsurance('IT', 250, 'IT safe insure', CorporateInsurancesType.CYBER_CASES,
                                       InsuranceType.CORPORATE, 72, 15000, 23,
                                       ['court', 'robbery', 'industrial accident'])
        obj_list = [self.obj1, self.obj2, self.obj3]
        self.insurance_manager = InsuranceManager(obj_list)

    def test_search_by_type(self):
        self.assertEqual(self.insurance_manager.search_by_type(InsuranceType.LIFE), [self.obj2])

    def test_sort_by_duration(self):
        self.assertEqual(self.insurance_manager.sort_by_duration(SortOrder.ASC), [self.obj1, self.obj2, self.obj3])

    def test_sort_by_risk(self):
        self.assertEqual(self.insurance_manager.sort_by_risk(SortOrder.DESC), [self.obj3, self.obj1, self.obj2])
