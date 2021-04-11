from models.insurance_type_list import InsuranceType
from models.property_list import Property
from models.benefits_list import Benefits
from models.types_insure import CorporateInsurance, LifeInsurance, PropertyInsurance
from models.corporate_list import CorporateInsurancesType
from manager.insurance_mang import InsuranceManager
from models.sort_order import SortOrder


def main():
    housing_insurance = PropertyInsurance(Property.HOUSE, 500000, 180000, 'Insure Housing', InsuranceType.PROPERTY, 24, 10000, 15,
                                     ['fire', 'robbery', 'tornado', 'burglary', 'flood'])
    people_insurance = LifeInsurance('John Jonson', 'Jack Billin', [Benefits.JURIDICAL_HELP], 'VSCU Safety', InsuranceType.LIFE, 36,
                                     15500, 12, ['deaths', 'car accident'])
    company_insurance = CorporateInsurance('IT', 250,'IT safe insure', CorporateInsurancesType.CYBER_CASES, InsuranceType.CORPORATE, 72,
                                      15000, 23, ['court', 'robbery', 'industrial accident'])

    manager1 = InsuranceManager([housing_insurance, people_insurance, company_insurance])
    print(manager1.search_by_type(InsuranceType.LIFE))
    print(manager1.sort_by_duration(SortOrder.ASC))
    print(manager1.sort_by_risk(SortOrder.DESC))


if __name__ == '__main__':
    main()
