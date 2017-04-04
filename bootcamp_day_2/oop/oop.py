class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = fname + '-' + lname + '@mail.com'

    def full_name(self):
        return '{} {}'.format(self.fname, self.lname)


class Tenant(Person):
    def __init__(self, fname, lname, amount_paid):
        super().__init__(fname, lname)
        self.amount_paid = amount_paid

class Property_owner(Person):
    def __init__(self, fname, lname, tenants=None):
        super().__init__(fname, lname)
        self.properties = {}
        if tenants is None:
            self.tenants = []
        else:
            self.tenants = tenants

    def add_tenant(self, ten):
        if ten not in self.tenants:
            self.tenants.append(ten)

    def add_property(self, property_id, description, street_address, rent_amount, owner):
        self.properties[property_id] = Property(property_id, description, street_address, rent_amount, self)
        return self.properties[property_id]

    def remove_tenant(self, ten):
        if ten in self.tenants:
            self.tenants.remove(ten)

    def print_tenant(self):
        for ten in self.tenants:
            print('-->', ten.full_name())


class Property:
    def __init__(self, property_id, description, street_address, rent_amount, owner):
        self.property_id = property_id
        self.description = description
        self.street_address = street_address
        self.rent_amount = rent_amount
        self.owner = owner
        self.owner.add_property(self)


tenant1 = Tenant('Sue', 'Jackson', 10000)
tenant2 = Tenant('Michael', 'Faraday', 5000)
landlord_1 = Property_owner('Ian', 'Smith', [tenant1])
property1 = landlord_1.add_property(1, '3 bedroomed house', '123 Kimathi', 30000)
print(landlord_1.full_name())
landlord_1.print_tenant()
print(landlord_1.add_property(1, '3 bedroomed house', '123 Kimathi', 30000))
