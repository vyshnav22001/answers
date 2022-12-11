import re

num = input('Enter a mobile number to validate: ')

Pattern = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$', re.VERBOSE)


if Pattern.match(num):

    print('Valid Mobile Number')
else:
	print("Invalid Mobile Number")


    #valid
    #+1 212.456.7890
    #212.456.7890
    #(212) 456-7890
    #212 456 7890
    #212-456-7890