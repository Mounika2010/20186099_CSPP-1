'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    len_str = len(str_input)
    count = 0
    temp = ""
    for char in len(str_input):
        if char in "!@#$%^&*":
            temp = count + " "
            count += 1
    print(temp)     
        
if __name__ == "__main__":
    main()
