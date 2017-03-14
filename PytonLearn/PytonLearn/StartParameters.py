import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-s', '--skip', default='0')
    parser.add_argument ('-t', '--take', default='0')
    parser.add_argument ('-m', '--mongo', default='')
 
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
print("Skip=",namespace.skip)
print("Take=",namespace.take)
print("MongoDB=",namespace.mongo)
