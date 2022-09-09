import distance

dist = distance.Distance(3)
print("3 kilometers is " + str(dist.miles) + " miles.")
dist.miles = 3
print(str(dist.miles) + " miles is " + str(dist.km) + " kilometers.")
