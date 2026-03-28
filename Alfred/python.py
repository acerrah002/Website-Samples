#x = "Blue"
#food = input("what is your favourite food?: ")
#print(x)
#print("Hi", food ,"is a really nice food")

#Comments dont effect code
#Data Types
#Alfred x2, Jeremy, a,




birdname = "Alfred"
print("..___")
print(".(`v`)")
print("((__))")
print("..^^")
#Human, Rocks, CinnamonToastCrunch, BirdFood
#Hard Rocks, Celery, Time Machines
favfoodone = "Otherbirds"
favfoodtwo= "Rocks"
favfoodthree= "CTC"
birdweight = 3
#Already won't fly past 10000 pounds
user = input("Would you like to feed Alfred?(y/n)")

if user == "y":
   print(favfoodone.favfoodtwo,favfoodthree)
   chooseforbird = input("what would you like to feed him")
   if chooseforbird == favfoodone:
      birdweight = birdweight + 2
      pass
   elif chooseforbird == favfoodtwo:
      birdweight = birdweight + 10
      pass
   elif chooseforbird == favfoodthree:
      birdweight = birdweight + 1
      pass
else:
    print("Bird ate you")
    birdweight= birdweight + 110