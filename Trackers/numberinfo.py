import phonenumbers
from phonenumbers import geocoder,carrier,timezone

def PhoneNumberTracker():
	print('')
	print("ENTER ALON WITH THE COUNTRY CODE FOR EG(+91)")
	print('')
	x = input("Enter the target Phonenumber: ")
	phonenumber = phonenumbers.parse(x)
	Country = (geocoder.description_for_number(phonenumber,"en"))
	Carrier = (carrier.name_for_number(phonenumber,"en"))
	Timezone = (timezone.time_zones_for_number(phonenumber))
	valid = phonenumbers.is_valid_number(phonenumber)
	possible = phonenumbers.is_possible_number(phonenumber) 

	print('')
	print(Country)
	print(Carrier)
	print(Timezone)
	print(valid)
	print(possible)


