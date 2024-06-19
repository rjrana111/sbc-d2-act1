b = "summber bootcamp"

print(b.title())

print(f"{b.capitalize().replace("p", "P")}")
replace1 = b.replace("b", "L")
print(f"{replace1[8:12]}")

print(f"{b[12:16].replace("p", "E")}")
#print(a.find("a"))
#print(a.find("r"))
print(f"{b[13].title()}{b[6].title()}")

print(b.replace(" ", "").isalpha)