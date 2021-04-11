from models.insurance_type_list import InsuranceType


class Insurance:
    def __init__(self, name: str, type_of_insurance: InsuranceType, duration_in_months: int, min_insurance_sum: float,
                 risk_level: int, insurance_events: list[str]):
        self.name = name
        self.type_of_insurance = type_of_insurance
        self.duration_in_months = duration_in_months
        self.min_insurance_sum = min_insurance_sum
        self.risk_level = risk_level
        self.insurance_events = insurance_events

    def __repr__(self):
        return " Name of insurance: {self.name} and type {self.type_of_insurance} ".format(self=self)
