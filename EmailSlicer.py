email=input("what is your email address?")
username=email[:email.index('@')]
domain=email[email.index('@')+1:]
print("Your username is " +username+ " and domain name is " + domain)
print("hrllo")