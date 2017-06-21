wrong_sets={} # This is wrong, it creates dictionary
right_sets=set()
tuple=()
list=[]

print(3.4 ** 2)
print(round(3.95,2))

courses=['History','Maths', 'DS','DBMS', 'Security']
print(courses.__len__())
courses.append('Art')
courses.insert(1,'SML')
print(courses)
courses.reverse()
print(courses)
courses.sort(reverse=True) #descending order
print(courses)

new_course=sorted(courses)
print(courses.index('DS'))
print(max(new_course))
print('Maths' in new_course)

course_str='- '.join(courses)
print(course_str)
print(course_str.split('-'))


