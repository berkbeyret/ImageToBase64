import base64
from urllib.request import urlopen
import sys
import os

os.system('mode con cols=100 lines=40' + bufferSize)

def welcome():
    print("""
####################################################################################################
##                                       ImagetoBase64                                            ##
##                Welcome to the console! You need to name the output file first.                 ##
##                                 And then enter the image url.                                  ##
##                 After entering the url  you need to specify the file type.                     ##
##                    After that console will convert the image to base64.                        ##
##                                                                                                ##
##                                     nauxnam 2020 ©                                             ##
####################################################################################################
""")

def base64func():
    namefile = input("Output name?: ")
    outputfile = open(namefile + '.txt', 'a')
    jpgprefix = 'data:image/jpg;base64,'
    pngprefix = 'data:image/png;base64,'
    bmpprefix = 'data:image/bmp;base64,'
    gifprefix = 'data:image/gif;base64,'
    target_url = input("Enter Image URL: ")
    dataimg = urlopen(target_url).read()
    filetype = input("Please specify the file type. (*.jpg,*.png,*.bmp,*.gif only.): ")
    if filetype.lower().strip() in 'jpg'.split():
        data = base64.b64encode(dataimg).decode('utf-8')
        print(jpgprefix + data, file=outputfile)
        print("Output has been written. Please chech the .txt file.")
        outputfile.close()
    elif filetype.lower().strip() in 'png'.split():
        data = base64.b64encode(dataimg).decode('utf-8')
        print(pngprefix + data, file=outputfile)
        print("Output has been written. Please chech the .txt file.")
        outputfile.close()
    elif filetype.lower().strip() in 'bmp'.split():
        data = base64.b64encode(dataimg).decode('utf-8')
        print(bmpprefix + data, file=outputfile)
        print("Output has been written. Please chech the .txt file.")
        outputfile.close()
    elif filetype.lower().strip() in 'gif'.split():
        data = base64.b64encode(dataimg).decode('utf-8')
        print(gifprefix + data, file=outputfile)
        print("Output has been written. Please chech the .txt file.")
        outputfile.close()
    else:
        print('Please enter the file types properly. File types must be lower-case character.')
    answer = input("Do you want to reload the console again? (y/n): ")
    if answer.lower().strip() in 'y'.split():
        base64func()
    elif answer.lower().strip() in 'n'.split():
        print("Exiting console...")
        sys.exit()
    else:
        print("Wrong input!!!")

welcome()
base64func()
