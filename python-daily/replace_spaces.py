def replaceSpaces(str):
    # Write your code here.
    temp = ""
    for x in str:
        if x==" ":
            temp+='@40'
        else:
            temp+=x
    return temp