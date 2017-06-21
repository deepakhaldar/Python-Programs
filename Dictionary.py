student={'name':'Deepak', 'age':24, 'phone':'555-987-1234', 'State':'Arizona'}
print(student.get('name'))

# False Values
# False, None, Zero of any numeric type
# Any empty sequence. For example, '', (),[].
# Any empty mapping. For example, {}
language={}
print(id(language))
print(id('Python'))
if language:
    print('Python')