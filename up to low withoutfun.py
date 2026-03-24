#upper to lower without function
s="G"
result=""
for c in s:
    result=result+chr(ord(c)+32)
print(result)


s="syeda "
result=""
for c in s:
    result=result+chr(ord(c)-32)
print(result)
