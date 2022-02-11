def areRotations(str1, str2):
	if(len(str1) != len(str2)):
		return 0;
	
	str11 = str1 + str1;
	if str2 in str11:
		return 1;
	return 0;

def main():
    # Your code goes here
	str1 = "ABACD"
	str2 = "CDABA"

	ans = areRotations(str1, str2);
	if ans==0:
		print("they are not rotations")
	else:
		print(str1, " and ", str2, " are rotations")
    
if __name__ == "__main__":
    main()

