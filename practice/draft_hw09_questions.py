#Draft CS5001 Homework 9 

#This is a list of sublists each containing two items: a person's name, list of their abilities (only one ability for now)
population = [  
	['Wax', ['Coinshot'] ] ,  
	['Marasi', [ 'Pulser'] ]  , 
	['Wayne', ['Slider'] ] 
	]


# Q1 - Turn the list into a dictionary (eg. abilities) where each sublist item translates into a key:value pair
# [name, [abilities...] ] translates to {name : [abilities...]} 
#Ans
abilities = {}  
for person in population:
	abilities.update({person[0]: person[1]})
print(abilities) 

# this creates a new entry in the dictionary since there is no Steris key
abilities.update({'Steris': ['TBD']})
# this updates (replaces) the value for the existing key "Wax"
abilities.update({'Wax': ['Coinshot', 'Skimmer']})



# Q2 - Update Wayne's abilities to : ['Slider', 'Bleeder']
#Ans
abilities.update({'Wayne': ['Slider', 'Bleeder']})
#updated {} = {'Wax': ['Coinshot', 'Skimmer'], 'Marasi': ['Pulser'], 'Wayne': ['Slider', 'Bleeder'], 'Steris': ['TBD']}



# Q3 - Write two expressions that print Marasi's list of abilities, one using the list population and the other using abilities dictionary
# What would be the runtime of each? (linear or constant time) Is one faster? Why?

#Ans
#Searching the dictionary is faster because we have instant access to each value via its unique/mapped key (constant time or O(1))
#Iteratating through the population list to locate 'Marasi' is an example of linear search since we have to traverse the list and
#check each item until we reach the sublist that has 'Marasi' as its first element
for person in population:  # using list, O(n)
	if person[0] == 'Marasi':
		print('Marasi\'s abilities include: %s ' % str(person[1]))

# using dictionary, O(1)
print('Marasi\'s abilities include: %s ' % str(abilities['Marasi']))



# Q4 - Display the population's list of abilities: Traverse the dictionary keys and store the values of the abilities
# in a list called vals. Print each person with their list of abilities ("Marasi's abilities include: ..."). 
# Lastly, print the resulting vals list.
#Ans
vals = []

for key in abilities:
	vals.append(abilities.get(key)) #store attributes in vals list
	print(key + '\'s' + ' abilities inlude: ' + str(abilities[key]))

# vals should contain [['Coinshot', 'Skimmer'], ['Pulser'], ['Slider', 'Bleeder'], ['TBD']]
print('Current list of this population\'s abiltiies: %s' % str(vals))



#Q5 - Create a 'Person' class with fields: name (type String), abilities (type list)
#accessor and mutator methods for name and abilties are provided

class Person:
	def __init__(self, name, abilities, profession = None):
		self.name = name
		self.abilities = abilities

	def getName(self):
		return self.name
	
	def getAge(self):
		return self.age

	def getAbilities(self):
		return self.abilities

	def setName(self, n):
		self.name = n

	def setAge(self, newAge):
		self.age = newAge

	# q - create a method to add to a Person's list of abilities
	def addAbility(self, a):
		self.abilities.append(a)

	# q - create a method to add a Person's profession 
	def createProfession(self, p):
		self.profession = p
        
    # q - create method to determine if Person has specified ability ab
	def hasAbility(self, ab):
		return ab in self.abilities

#Below are three Person objects, the abilities list fields are assigned by accessing the abilities dictionary
wayne = Person('Wayne', [abilities.get('Wayne')])
marasi = Person('Marasi', [abilities.get('Marasi')])
steris = Person('Steris', [abilities.get('Steris')])


# Q6 - create a Person object (eg. wax), once object is created use your methods to update Wax's profession to 'Lawman'
#create additional Person object
wax = Person('Wax', [abilities.get('Wax')] ) 
wax.createProfession('Lawman')


# TO DO test functions, optional paramters
print(wax.abilities)  # check updated wax obj fields
print(wax.profession)





