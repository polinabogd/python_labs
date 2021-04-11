from .insurance import Insurance
from .corporate_list import CorporateInsurancesType
from .benefits_list import Benefits
from .insurance_type_list import InsuranceType
from .property_list import Property


class CorporateInsurance(Insurance):
    def __init__(self, business_field: str, employee_amount: int, name: str, insurance_type: CorporateInsurancesType,
                 type_of_insurance: InsuranceType, duration_in_months: int, min_insurance_sum: float, risk_level:
            int, insurance_events: list):
        super().__init__(name, type_of_insurance, duration_in_months, min_insurance_sum, risk_level, insurance_events)
        self.business_field = business_field
        self.employee_amount = employee_amount
        self.insurance_type = insurance_type




class LifeInsurance(Insurance):
    def __init__(self, person_name: str, inheritor_name: str, guaranteed_benefits: list[Benefits], name: str,
                 type_of_insurance: InsuranceType, duration_in_months: int, min_insurance_sum: float, risk_level:
            int, insurance_events: list):
        super().__init__(name, type_of_insurance, duration_in_months, min_insurance_sum, risk_level, insurance_events)
        self.person_name = person_name
        self.inheritor_name = inheritor_name
        self.guaranteed_benefits = guaranteed_benefits


class PropertyInsurance(Insurance):
    def __init__(self, type_of_property: Property, property_price: int, max_payment: int, name: str,
                 type_of_insurance: InsuranceType, duration_in_months: int, min_insurance_sum: float, risk_level:
            int, insurance_events: list):
        super().__init__(name, type_of_insurance, duration_in_months, min_insurance_sum, risk_level, insurance_events)
        self.type_of_property = type_of_property
        self.property_price = property_price
        self.max_payment = max_payment
