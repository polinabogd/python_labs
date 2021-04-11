from models.insurance import InsuranceType
from models.sort_order import SortOrder


class InsuranceManager:
    def __init__(self, insurances: []):
        self.insurances = insurances

    def sort_by_risk(self, order_to_sort: SortOrder):
        return sorted(self.insurances, key=lambda Insurance: Insurance.risk_level, reverse=bool(order_to_sort.value))

    def sort_by_duration(self, order_to_sort: SortOrder):
        return sorted(self.insurances, key=lambda Insurance: Insurance.duration_in_months, reverse=bool(order_to_sort.value))

    def search_by_type(self, type: InsuranceType):
        new_insurances = []
        for insurance in self.insurances:
            if insurance.type_of_insurance == type:
                new_insurances.append(insurance)
        return new_insurances
