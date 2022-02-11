first = -1
last = -1
def findOccurence(str_input, idx, ele):
  global first
  global last
  if idx==len(str_input):
    print("first=", first, "last=", last)
    return
  
  if(str_input[idx]==ele):
    if first==-1:
      first = idx
    else:
      last = idx

  findOccurence(str_input, idx+1, ele)
  

if __name__=="__main__":
  str_input = "abaacdaefaah"
  findOccurence(str_input, 0, 'a')