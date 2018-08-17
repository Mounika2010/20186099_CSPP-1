'''
clean string
'''
import re
s = "hellooerghtj!!!"
s = s.lower().strip()
regex = re.compile('[^a-z]')
print(regex.sub(" ", s).split(" "))
