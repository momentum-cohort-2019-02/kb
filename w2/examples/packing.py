print("Let's weigh some luggage!")
max_weight = 100
total_weight = 0

more_bags = True
while more_bags:
    weight = input("What's the weight of your bag? " +
                   "(Hit enter to finish.) ")

    if weight == "":
        more_bags = False
    else:
        total_weight = total_weight + int(weight)
        print("Current total weight is " + total_weight + ".")

print("Your total weight is ", total_weight, ".")
if total_weight > max_weight:
    print("You are " + total_weight - max_weight +
          " pounds over the allowed weight.")
