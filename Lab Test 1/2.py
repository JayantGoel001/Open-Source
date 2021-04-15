import matplotlib.pyplot as plt

d = {
    1: {
        "id": 1,
        "name": "AI",
        "location": ["GZB", "Mumbai"],
        "department": "Mechanics",
        "profit": 2000.00
    }, 2: {
        "id": 2,
        "name": "JAVA",
        "location": ["NOIDA", "Mumbai", "Chennai", "GZB"],
        "department": "MATHS",
        "profit": 99300.00
    }, 3: {
        "id": 3,
        "name": "C++",
        "location": ["Delhi", "Chennai"],
        "department": "Software",
        "profit": 28053.00
    }, 4: {
        "id": 4,
        "name": "Python",
        "location": ["Los Angelos", "Delhi"],
        "department": "Software",
        "profit": 9000.00
    }, 5: {
        "id": 5,
        "name": "Archade",
        "location": ["Chennai", "Delhi"],
        "department": "Software",
        "profit": 3500.00
    }
}

# 1
maxProfit = 0
maxProfitDetails = {}
for uid, details in d.items():
    if details["profit"] > maxProfit:
        maxProfitDetails = details
        maxProfit = details["profit"]
print("project having maximum profit")
print(maxProfitDetails)

# 2
maxLoc = 0
maxLocationDetails = {}
for uid, details in d.items():
    if len(details["location"]) > maxLoc:
        maxLoc = len(details["location"])
        maxLocationDetails = details

print("Project Running at maximum location")
print(maxLocationDetails)

# 3
department = {}
for uid, details in d.items():
    if details["department"] not in department:
        department[details["department"]] = 0

    department[details["department"]] += 1
print("Dapartment")
print(department)

print("Department having minimum Project")
minPro = 9999999999999
minDepartment = ""
for key, value in department.items():
    if value < minPro:
        minDepartment = key
        minPro = value

print(minDepartment)

# 4
print("Question 4")
for uid, details in d.items():
    print(uid, "--->")
    print("Project Name:", details['name'].upper())
    print("Location:")
    for loc in details['location']:
        print(loc[0].upper() + loc[1:])

# 5
add = 0
for uid, details in d.items():
    add += details['profit']

avgProfit = add / len(d)
print("Average:", avgProfit)

print("Project with profit less than average")
for uid, details in d.items():
    if details["profit"] < avgProfit:
        print(details)

# 6

plt.bar(department.keys(), department.values())
plt.show()
