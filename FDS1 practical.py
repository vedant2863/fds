"""
In second year computer engineering class, group A student’s play cricket, group B students
play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.

(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-
in functions)
"""


#A
def intersection (l1,l2):
	res=[]
	for student in l1:
		if student in l2:
			res.append(student)
	return res  

                     
a=[1,2,3,4,5,6,7]
b=[2,3,6,7,10]
c=[2,4,6,8,10,12]
print(f"A={a}|\nB={b}|\nc={c}\n")
print(f"a",end=" ")
print(intersection(a,b))

def union (l1,l2):
	res=l2.copy()
	for student in l1:
		if not student in l2:
			res.append(student)
	return res	
	
#B
def diff (l1,l2):
	res=[]
	for student in l1:
		if not student in l2:
			res.append(student)
	return res
u=union(a,b)
i=intersection(a,b)
print(diff(u,i))

#C
diffcb=diff(c,b)

print(diff(diffcb,a))

#D
unionac=union(a,c)
print(diff(unionac,b))