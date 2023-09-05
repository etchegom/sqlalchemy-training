import factory

from sqla_training.models import User, Vehicle


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User

    firstname = factory.Faker("first_name")
    lastname = factory.Faker("last_name")
    phone_number = factory.Faker("phone_number")
    personal_info = factory.Faker("sentence")

    @factory.post_generation
    def addresses(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for address in extracted:
                self.addresses.add(address)


class AddressFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User

    email_address = factory.Faker("email")
    user = factory.SubFactory(UserFactory)


class VehicleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Vehicle

    user = factory.SubFactory(UserFactory)
    model = factory.Faker("vehicle_make_model")
