import datetime
Year= eval(input("Enter Your Born Year:"))
Month= eval(input("Enter your Born Month:"))
Date= eval(input("Enter your Born date"))

DOB=datetime.datetime(Year,Month,Date)
Age=(datetime.datetime.now()-DOB)

print(Age)