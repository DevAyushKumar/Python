'''Creating command line utility in Python: 
Command line utilities are programs that can be run from the terminal or command line interface, and they are essential part of many development workflows. In python, you can create your own command line utilites using the built in argparse operator.'''

#syntax
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("url", help = "url of the file download")
parser.add_argument("output", help= "by which name do you want to save your file")

args = parser.parse_args()

print(args.url)
print(args.output)

'''Adding optional arguments:
The following example shows how to add optional arguments in python'''

#syntax
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--optional", help= "description of optional argument", default= None)
args = parser.parse_args()

print(args.optional)