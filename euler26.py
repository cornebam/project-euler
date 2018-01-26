import re
r = re.compile(r"(.+?)(?=\1)")
print(r.findall("absabcabc"))
