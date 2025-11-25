# Parsing unstructured daycare text into a simple structured format

data = """
Center/Daycare
825 23rd Street South
Arlington, VA 22202
703-979-BABY (2229)
22.
Maria Teresa Desaba, Owner/Director; Tony Saba, Org. Director.
Web site: www.mariateresababies.com
Serving children 6 weeks to 5yrs full-time.

National Science Foundation Child Development Center
23.
4201 Wilson Blvd., Suite 180 22203
703-292-4794
Web site: www.brighthorizons.com 112 children, ages 6 wks-5 yrs.
7:00 a.m. - 6:00 p.m. Summer Camp for children 5-9 years.
"""

lines = [line.strip() for line in data.split("\n") if line.strip()]

center1 = {
    "Name": lines[0],
    "Address": lines[1],
    "City_State_Zip": lines[2],
    "Phone": lines[3],
    "Code": lines[4],
    "Directors": lines[5],
    "Website": lines[6].replace("Web site: ", ""),
    "Details": lines[7],
}
center2 = {
    "Name": lines[8],
    "Code": lines[9],
    "Address": lines[10],
    "Phone": lines[11],
    "Website": lines[12]. replace("Web site: ", ""),
    "Hours": lines[13]
}
print("Formatted Center Information:\n")
print("Center 1:")
for key, value in center1.items():
    print(f"{key}: {value}")

print("Formatted Center Information:\n")
for key, value in center2.items():
    print(f"{key}: {value}")
