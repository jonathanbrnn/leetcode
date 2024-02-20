s = "The sky is blue"
temp = s.split()
sol = ""
for word in temp[::-1]:
    sol+= word + " "
print(sol[:-1])
