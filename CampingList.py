#Hey, we're going on a camping trip!

#Here is the stuff we will need

#tent, sleeping bags, water, raspberry pi, coffee, knie, ethernet cable, flash drive, beard oil, marshmallows

camping_stuff = "tent, sleeping bags, water, raspberry pi, coffee, knie, ethernet cable, flash drive, beard oil, marshmallows"

#print(camping_stuff)

#Python List:

camping_list = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 89.3, True]

me = camping_list[4]
friend = camping_list[-2]

#print(me)
#print(friend)

#print(camping_list)


#append method only allows one new piece of data to be added at a time
#camping_list.append("toilet paper")
#camping_list.append("bidet")

#extend method allows to "extend" the list by adding more to it, see: brackets / add a new list to an existing list
#camping_list.extend(["toilet paper", "bidet"])

#alternative way:
#camping_list = camping_list + ["toilet paper", "bidet"]

#adding new list in a specific spot on the already created list:
camping_list.insert(0, "bidet")
camping_list.insert(-1, "toilet paper")

#Removing stuff with Python commands
#Command below removes everything from said list
#camping_list.clear()

#Command below removes a specific piece af data
#camping_list.remove("tent")
#camping_list.remove("sleeping bags")

#Command below will remove pieces of data from list via index numbers
#camping_list.pop(0)
#camping_list.pop(0)

#.pop command will return the value of the index that was removed
print("This items was just deleted: " + camping_list.pop(0))

print(camping_list)