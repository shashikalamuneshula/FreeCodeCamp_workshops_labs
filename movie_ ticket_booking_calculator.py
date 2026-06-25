# movie ticket booking calculator
base_price = 15  # price of the ticket
age = 21  # age of the user
seat_type = 'Gold'
show_time = 'Evening'

# check if the user eligible to book a ticket or not
if age > 17:
    print('User is eligible to book a ticket')
    if age >= 21:
        print('User is eligible for evening shows')
    else:
        print('User is not eligible for evening shows')
else:
    print('User is not eligible to book a ticket')

# check whether user has membership or not
is_member = True  # user in membership
is_weekend = False  # whether movie show on a weekend

# check whether user qualifies for membership discount if they are a member
discount = 0
if is_member and age > 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

print('Discount:', discount)

# calculate extra charges
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

print('Extra charges:', extra_charges)

# confirm/decline booking
if age >= 21 or (age >= 18 and (show_time == 'Evening' or is_member)):
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
        
    print('Service charges:', service_charges)
    final_price = (base_price + extra_charges + service_charges) - discount
    print('Final price of ticket:', final_price)
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')
