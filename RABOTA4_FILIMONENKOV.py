
#1
Name = "Sergey"
Secondname = "Filimonenkov"
Yearbirth = "2003"

print(name,secondname,yearbirth, sep = "_")

#2
print("Enter catets: ")
a = int(input())
b = int(input())
c = (a**2 + b**2)**0.5
print("Ploshad =",(a*b/2)
print("Perimetr =", a+b+c)

#3
print("Enter radius: ")
radius = int(input())
print("Ploshad =", radius**2 * 3.14)

#4
print("How many years - ", end = "")
years = int(input())

time = years * 365 * 24 * 60
print("Time in minutes -", time)
print("You will see", time//5, "exponauts")

print("How many exponats - ", end = '')
exponauts = int(input())

print(exponauts * 5, "minutes to see these")
print(exponauts * 5 / 60, " hours you need")
print(exponauts * 5 / 60 / 24, "days you need")
print(exponauts * 5 / 60/ 24 / 365, "years you need")













