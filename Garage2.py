# I worked REALLY hard  on this code, and I'm quite pround of how concise I got it.  DAYS it took.  DAYS!  Please try to fool it when you run it!  

class Parking_Garage:
    def __init__(self):
        self.available_tickets = list(range(1, 51))
        self.available_spaces = list(range(1, 51))
        self.current_ticket = {}

    def takeTicket(self):
        ticket = self.available_tickets.pop(0)
        space = self.available_spaces.pop(0)
        self.current_ticket[ticket] = {'paid': False}
        print(f"Your ticket number is {ticket} and your parking space is {space}")

    def payForParking(self):
        payment_incomplete = True
        while payment_incomplete:
            user_ticket = int(input('please enter your ticket number '))
            if user_ticket in self.current_ticket.keys():
                while True:
                    payment = int(input("Please enter $20 for parking payment: "))
                    if payment == 20:
                        self.current_ticket[user_ticket]['paid'] = True
                        print("Your ticket has been paid. You have 15mins to leave.")
                        payment_incomplete = False
                        break
                    elif payment > 20:
                        change = int(payment) - 20
                        self.current_ticket[user_ticket]['paid'] = True
                        print(f'Please take your ${change} change')
                        payment_incomplete = False
                        break
                    else:
                        print("Insufficient payment. Please try again.")
            else:
                print('That ticket is not currently in use.')


    def leaveGarage(self):
        user_has_left = False
        while not user_has_left:    
            user_ticket = int(input('please enter your ticket number '))
            if user_ticket in self.current_ticket.keys():
                while True:
                    if self.current_ticket[user_ticket]['paid']:
                        print("Thank You, have a nice day.")
                        self.available_tickets.append(user_ticket)
                        self.available_spaces.append(user_ticket)
                        del self.current_ticket[user_ticket]
                        user_has_left = True
                        break
                    else:
                        print("Your ticket has not been paid. Please pay before leaving.")
                        self.payForParking()
            else:
                print('That ticket is not currently in use.')

   
    def view_current_tickets(self):
        print("Current tickets:", self.current_ticket)


garage = Parking_Garage()


garage.takeTicket()
garage.payForParking()
garage.leaveGarage()