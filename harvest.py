############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, 
                 is_bestseller):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings = pairing

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    cas.add_pairing('strawberries and mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        print(f'- {melon.pairings}')

    return None

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}

    for melon in melon_types:
        key = melon.code
        value = melon
        melon_dict[key] = value

    return melon_dict  

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):

        if self.harvested_from != 3:
            if self.shape_rating > 5 and self.color_rating > 5:
                self.is_sellable = True
            else:
                self.is_sellable = False
        else:
            self.is_sellable = False


def make_melons(melon_types):
    """Returns a list of harvested Melon objects."""
    harvested_list = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    harvested_list.append(melon_1)
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    harvested_list.append(melon_2)
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    harvested_list.append(melon_3)
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Michael')
    harvested_list.append(melon_4)
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    harvested_list.append(melon_5)
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    harvested_list.append(melon_6)
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    harvested_list.append(melon_7)
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    harvested_list.append(melon_8)
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    harvested_list.append(melon_9)

    return harvested_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        melon.is_sellable()
        if melon.is_sellable:
            sell = '(CAN BE SOLD)'
        else:
            sell = '(NOT SELLABLE)'
        print(f'Harvested by {melon.harvested_by} from Field {melon.harvested_from} {sell}')    


melon_types = make_melon_types()

melons_by_id = make_melon_type_lookup(melon_types)

melons = make_melons(melon_types)
