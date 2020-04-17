# Variables
friends = ["Magnus", "Anders", "Andreas", "Thomas", "Mads"]

print(friends)
print(friends[0])
print(friends[-2])
print(friends[1:])
friends[1] = "Gud"
print(friends[1:3])

print()

lucky_numbers = [4, 8, 15, 16, 23, 42]

friends.append("Creed")
print(friends)

friends.insert(1, "Anders")
print(friends)

friends.sort()
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.remove("Gud")
print(friends)

friends.pop()
print(friends)


print(friends.index("Magnus"))

print(friends.count("Magnus"))

friends.reverse()
print(friends)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)
