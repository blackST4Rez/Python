# users = ['dave', 'john', 'raka']

# data = ['raka', 34, True, 456]

# emptylist = []

# print('dave' in data) # here dave is not in the list named data

# print(users[1]) # prints second value of the list
# print(data[-1]) # prints last value of the list

# print(users.index('raka')) # prints the index of raka from the list users

# print(users[0:2])
# print(users[1:])
# print(users[-3:-1])

# print(len(data)) #prints the length of the lists

# users.append('jimmy') # adds jimmy to the list and prints it
# print(users)

# users += ['jason'] # adds jason to the list and prints it
# print(users)

# users.extend(['sam', 'sara']) # adds users to the list and prints it
# print(users)

# users.extend(data) # passes the list data into the other lists
# print(users)

# users.insert(0, 'crazy')
# print(users)

# users[2:2] = ['eddie', 'alex'] # shift the value inside the list
# print(users)

# users[1:3] = ['jamal', 'sonny'] # replace the value inside the list
# print(users)

# users.remove(456) # remove the specific value from the list via parameter
# print(users)

# print(users.pop()) # removes the last value from the list 
# print(users)

# del users[0] # delete user with their index of the list
# print(users)

# # del data # delete the whole list 
# # print(data)

# data.clear() # delete just the data inside list 
# print(data)

# users[1:2] = ['maka']
# users.sort()
# print(users)

# users.sort(key = str.lower)
# print(users)

# nums = [2,3,1,123,1,4,34,2]
# nums.reverse()
# print(nums)

# nums.sort( reverse=True)
# print(nums)

# print(sorted(nums, reverse=True))
# print(nums)

# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]

# print(numscopy)
# print(mynums)
# mycopy.sort()
# print(mycopy)
# print(nums)

# Tuples

mytuple = tuple(('raka', 0 , True))
anothertuple = (1, 2, 3, 4, 5)

# print(mytuple)
# print(anothertuple)
# print(type(mytuple))
# print(type(anothertuple))

newlist = list(mytuple)
newlist.append('neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))