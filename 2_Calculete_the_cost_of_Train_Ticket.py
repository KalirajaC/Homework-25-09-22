# Calculate the cost of train ticket
print("From Madurai to Chennai")
ticket=int(input("\n Enter how many ticket :"))
return_ticket=input("\n Type yes if you need return ticket : ")

def Tot_amt(m1,m2):
    total=ticket*1000
    return_total=ticket*750
    if ticket<=3:
        print("\n Your total amount for the ticket is :",total)
    if return_ticket==('yes' or "YES" or 'Yes'):
        print("\n Your total amount for the ticket is :",return_total+total)
    if ticket>=4:
        discount=total*(20/100)
        print("\n Your total amount for the ticket(with discount) is :",int(total-discount))
    if ticket>=4 and return_ticket==('yes' or "YES" or 'Yes'):
        discount_percent=total*(20/100)
        discount=int(total-discount_percent)
        print("\n Your total amount for the ticket(with both return and discount) is :",discount+return_total)
Tot_amt(ticket,return_ticket)
