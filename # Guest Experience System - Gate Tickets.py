# Guest Experience System - Gate Tickets Module


# Define the ticket prices.
ticket_prices = (
    "Rider": 29.99,
    "Non-Rider": 9.99,
    "Senior": 16.99,
    "Child": 0
)

# Define the discount rates.
discount_rates = {
    "Rider": 0.2,
    "Non-Rider": 0.2,
    "Senior": 0.2,
    "Child": 
}

ticket_types = []
discount_tickets = ()

#Lead Guest Name
def get_guest_name():
    flag = true

    while flag:
        guest_name = input("Lead Guest Name: ")

        #add validation to check if input is alphanumeric
        if guest_name.isalphanumeric() == False:
            print("Sorry you have not entered a recognised name.")
            flag = True
        else:
            guest_name = format(guest_name.capitalize())
            flag = False

    return guestname

#Date of visit
def get_visit_date()
    flag = True

    while flag:
        #enter date of visit
        visit_date = input("Date of Visit (DD-MM-YYYY): ")

        #check format of input date
        date_format = "%d-%m-%Y"

        #check if date is in correct format
        try:
            res = bool(datetime.strptime(visit_date, date_format))
        except ValueError:
            res = False

        #check if date is in the future
        current_date = datetime.now()
        past = datetime.strptime(visit_date, "%d-%m-%Y")

        if past.date() > current_date.date():
            res2 = True
        else:
            res2 = False

        if res and res2:
            flag = False
            return visit_date
        else:
            print("Date invalid. Please enter a date in the future.")


#Number of Guests
def get_num_guests():
    flag = True

    while flag:
        guest_number = input("Number of Guests in Party: ")

        #check user has entered an integer
        try:
            guest_number = int(guest_number)
            flag = False
        
        except ValueError:
            print("Please enter a whole number")
    
    return guest_number

 
#Ticket Types
def guest_tickets(num_guests):

    flag = True
    print("")
    print("All guests must have a ticket.\n")
    print("Available tickets: Rider (R), Non-Rider (N), Senior (S), Child under 90cm (C)\n")
    for i in range(num_guests):
        
        while flag:
            ticket_type = input("Enter the ticket type for guest {}: ".format(i + 1))
            ticket_type = ticket_type.upper()

            #check if valid ticket type entered
            if ticket_type == "R":
                ticket_type = "Rider"
                break
            elif ticket_type == "N":
                ticket_type = "Non-Rider"
                break
            elif ticket_type == "S":
                ticket_type = "Senior"
                break
            elif ticket_type == "C":
                ticket_type = "Child"
                break
            else:
                print("Please enter a valid ticket type: R, N, S or C")

        ticket_types.append(ticket_type)

#Calculate subtotal
def calculate_subtotal():
    # Calculate the subtotal.
    subtotal = 0
    for ticket_type in ticket_types:
        subtotal += ticket_prices[ticket_type]
    
    return subtotal

#Calculate discount
def calculate_discount(subtotal):

    # Calculate the discount.
    discount = 0
    total_discount = 0

    #calculate discounted price for each ticket   
    for ticket_type in ticket_types:
        discount += ticket_prices[ticket_type] / discount_rates[ticket_type]
        discount = round(discount, 2) # round to 2dp
        discount_tickets.append(discount)
        discount = 0

    #calculate total discount
    for discount in discount_tickets:
        total_discount += discount
    
    return total_discount


#print booking summary
def print_summary(subtotal, discount, final_total):
    # Print booking summary
    print("")
    print("##############################################")
    print("############## Booking Summary  ##############")
    print("##############################################")
    print("")
    print("Visit Details")
    print("Lead Guest Name:", lead_guest_name)
    print("Date of Visit:", date_of_visit)
    print("Number of Guests in Party:", num_guests)
    print("\nTicket Details")
    for ticket_type in ticket_types:
        print("{} Ticket: Â£{:.2f}".format(ticket_type, ticket_prices[ticket_type]))
    print("\nSubtotal (before discounts): Â£{:.2f}".format(subtotal))
    print("Advanced Booking Discount: Â£{:.2f}".format(discount))
    print("Total to Pay: Â£{:.2f}".format(final_total))


#Start Program
enter_booking = True

while enter_booking:

    print("")
    print("###############################################")
    print("###### Fun Land Guest Experience System  ######")
    print("###############################################")
    print("")
    print("############# Select an Option ################")
    print("")
    print("1. Enter Guest Booking")
    print("2. View Booking Details")
    print("3. Exit")
    print("")
    
    main_choice = int(input("Enter option here: "))

    if main_choice == 1:

        # Get Guest Details
        lead_guest_name = get_guest_name()
        date_of_visit = get_visit_date()
        num_guests = get_guest_name()

        # Get Ticket Details
        guest_tickets(num_guests)

        #Discount applied to advanced bookings
        advanced = input("Is this an advanced booking? Y/N ")
        advanced = advanced.upper()
    
    elif main_choice == 2:
        #calculate subtotal
        subtotal = calculate_subtotal()

        #check if a guest booking has been entered
        if ticket_types != []:
            if advanced == 'N':
                #calculate online discount
                calculated_discount = calculate_discount(subtotal)
            else:
                calculated_discount = 0
       
            #calculate total to pay
            final_total = subtotal - calculated_discount
       
            #print booking summary
            print_summary(subtotal, calculated_discount, final_total)
        
            #clear lists
            ticket_types.clear() 
            discount_tickets.clear()
        else:
            print("No booking details to display")
    
    elif main_choice == 3:
        #exit the program
        exit()
    
    else:
        print("Please enter a valid choice 1-3")