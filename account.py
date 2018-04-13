class Value:

    def __init__(self):
        self.amount = 0

    @staticmethod
    def _prepare_amount(value, commission):
        return value - value * commission

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = self._prepare_amount(value, obj.commission)

class Account:

    def __init__(self, commission):
        self.commission = commission

    amount = Value()
