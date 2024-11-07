import re

#Split the string at every white-space character:

txt = "The rain, in Spain"
x = re.split(r"([\s,]+)" , txt)
y = x[1::2]
print(x,y)
