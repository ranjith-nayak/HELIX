from faker import Faker

fake = Faker("en_IN")

print("HELIX Environment Ready!")

print(fake.name())
print(fake.email())
print(fake.phone_number())