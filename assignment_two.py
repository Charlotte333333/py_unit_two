name = input("What is your name?")
print("That's a beautiful name", name)

you = input("How are you today?")
if you.find("bad")!=-1:
    print("Im sorry about that. If it makes you feel better Taylor swift is dropping a new album October 21st!!")
else:
    print("okay,cool. I am feeling good because Taylor is releasing a new album in late October!!")


artist=input("Whats your fav music artist?")
if artist.find("taylor")!=-1:
    print("I LOVE TAYLOR")
else:
    print("oh...okay. You should liten to Taylor Swift! She's really good.")

concert = input("If you went to a concert which concert whould it be?")
if concert.find("taylor")!=-1:
    print("I WAS GONNA BUY TICKETS TO HER CONCERT! But its so expensive")
else:
    print("okay, I hear those tickets are expensive.")

cost = float(input("how much would those tickets cost?"))
print("JEEZ!")

length = int(input("How long is your loan in years?"))
monthlyLength = length * 12

annualIntrestRate = float(input("How much is your annual interest rate?"))
r= float((annualIntrestRate/100)/12)
monththlypayment = ((r * cost) / (1 - ( 1 + r) ** -monthlyLength))
print(round(monththlypayment,2))
totalCost = (monththlypayment*monthlyLength)

print("Your monthly payment for the concert is ",monththlypayment , "that is a total of" ,totalCost,"")

print("bye ",name,"")















