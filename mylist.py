trainees = ["John",[2,["James","Mary"]]]
print("Original list",trainees)
print(trainees[1][1][0])


trainees.append(56)
print(trainees)


trainees[1][0] = 8 
print(trainees)

trainees.remove("John")
print(trainees)

print(len(trainees))

