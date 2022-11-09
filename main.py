import os
import csv

"""
The program is designed to replace the product ID with the product ean code -> 
It is useful when integrating the online store with the Amazon Vendor sales system.

To execute the program, we need a CSV file with 2 items, e.g .:

Product Code1, Code Ean1
Product Code2, Code Ean2

If there are two same files, but described e.g. 7441, 7441_2, 7441_5 (e.g. the same photo, but slightly modified), 
then the EAN code will be completed similarly:
0000000000000.MAIN, 0000000000000_1, 0000000000000_2 etc.
"""

x = 1
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for file in sorted(os.listdir()):
        for productId, ean in reader:
            if ean + ".MAIN" + ".jpg" not in os.listdir():
                x = 1
                try:
                    os.rename(productId, ean + ".MAIN" + ".jpg")
                    print("File: ", productId, " was properly renamed to ", ean + ".MAIN.jpg")
                except Exception as error:
                    print("Error occured:  ", error)
            else:
                try:
                    g = ean + "_" + str(x)
                    os.rename(productId, g + ".jpg")
                    print("File: ", productId, " was properly renamed to ", g + ".jpg")
                    x += 1
                except Exception as error_2:
                    print("Error occured:  ", error_2)
