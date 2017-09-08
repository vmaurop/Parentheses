#coding=utf8
status = "ok"
user_input=""
while not user_input: 
    user_input = raw_input ("Give a sequence of parentheses: ")
stack = ""
for i in user_input:
    if i == "(":
        stack = stack + i
        continue
    if i == ")" and stack.endswith("("):
        stack = stack[:-1]
        continue
    if i == ")" and not stack.endswith("("):
        status = "error"
        break
    print "Unrecognizable character: " + i
    status = "error"
    break
if not stack and status == "ok":
    print ("\nTrue")
else:
    print ("\nFalse")



