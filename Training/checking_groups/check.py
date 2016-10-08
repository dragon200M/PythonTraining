#!/usr/bin/python3.5

def group_check(s):

    if len(s) % 2 == 0:
        lista=list(s)
        stack = []
        for i in range(len(s)):
            c=s[i]


            if c == "(" or c == "{" or c == "[":
                stack.append(c)
                print(stack)
            elif c == ")":

                if isEmpty(stack):return False
                if stack.pop() != "(":return False
            elif c == "}":
                if isEmpty(stack):return False
                if stack.pop() != "{":return False
            elif c == "]":
                if isEmpty(stack):return False
                if stack.pop() != "[":return False

        return isEmpty(stack)
    else:
        return False




def isEmpty(li):
    if not li:
        return True
    else:
        return False





