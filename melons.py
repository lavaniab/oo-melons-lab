"""Classes for melon orders."""


class AbstractMelonOrder():
    """serve as a base class and refactor"""
# christmas melons 1.5 times base price
# international orders are +$3 if order less than 10 melons
    species = ['christmas_melon', 'muskmelon', 'watermelon']

    def get_total(self, species):
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        for specie in species:
            if species == 'christmas_melon':
                base_price = base_price * 1.5
        return total

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty


class DomesticMelonOrder():
    """A melon order within the USA."""

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #    self.shipped = False
    def __init__(self, order_type, tax):
        self.order_type = "domestic"
        self.tax = 0.08

    # def get_total(self):
        """Calculate price, including tax."""

        # base_price = 5
        # total = (1 + self.tax) * self.qty * base_price

        # return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder():
    """An international (non-US) melon order."""

    def __init__(self, country_code, shipped, order_type, tax):
        """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    # def get_total(self):
        """Calculate price, including tax."""

        # base_price = 5
        # total = (1 + self.tax) * self.qty * base_price

        #  return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    # passed_inspection = False

    def __init__(self, mark_inspection):
        passed_inspection = False
        self.mark_inspection = mark_inspection
        # mark_inspection = input('> ')
        if mark_inspection == 'passed':
            passed_inspection = True

        return passed_inspection
