## COP3410- Lecture 3
## Control Structures and Functions
## Date : 08/30/2024


######################################################
##grade = int(input("enter your final grade out of 100 >> "))
##final = 'X'
##if 90 <= grade <= 100:
##    final = 'A'
##elif 80 <= grade :
##    final = 'B'
##elif 70 <= grade :
##    final = 'C'
##else:
##    final = 'F'
##print('final grade: ', final)
##
##
#### practice the Boolean branching statements ########
##
##door_is_closed =  True
##
##if door_is_closed:
##    open_door =  True
##    door_is_closed =  False
##advance = True
##
##print("door:\n", "Closed?", door_is_closed,"\n", "Open?", open_door,"\n", "advance? ", advance,"\n")
####
####
######################## nested structure using closed and locked doors ##############################
##
##door_is_closed =  True
##door_is_locked = True
##unlock_door = False
##advance = False
##
##if door_is_closed:
##    if door_is_locked:
##        unlock_door = True
##    open_door = True
##advance = True
##
##print("door:", "closed?", door_is_closed,"locked?", door_is_locked, "now unlocked?", unlock_door, "ready to advance?", advance, sep = '\n')


########################## while loop : Find the letter 'X' in the text. ########################################
##
##data = input("enter any string, we're looking for the first apprearance of an X: ")
##j = 0
##data = data.upper()
##while j < len(data) and (data[j] != 'X'):
##    j += 1
##
##if j <= len(data):
##    print('found an X at location ', j+1)
##else:
##    print('No X!')

############################# function definition: count would count the number of occurences of a target value in data #######
##def count(data, target):
##    n = 0
##    for item in data:
##        if item == target: # found a match
##            n += 1
##    return n
##
############### function call ####################
##x = count( [1,2,3,4,9,9,9], 9)
##print( x)
##
##
##
####################### List Comprehension Example ########################
##n = 200
##total = sum(k *k for k in range(1, n+1))
##print('''Total is computed using list comprehension,
##        memory is not wasted,
##        only one object is calculated''', total)
	

######################Generators###########################################
def factors(n):
    for k in range(1,n+1):
        if n%k == 0:
            yield k
            print(type(k))
    return k

factors(4)
result = factors(4)
print(type(result))

##### Use the generator as an iterator ##################################
print("Objects that the generator created are now being iterated over: \n")
for i in result:
    print(i)
            
        




