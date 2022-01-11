#!/bin/python3
# A basic python script to extract js files from a log and sort
# TODO: Add support for other file extensions
# TODO: Add support for multiple files
# TODO: Add the ability to specify file location
# TODO: Add error handling 


# Must be run in the directory with the log file

filenames = set()

with open(r"access_log.txt") as file:
    for line in file:
        end = line.rfind(".js") + 3
        start = line.rfind("/", 0, end) + 1
        filename = line[start:end]
        if filename.endswith(".js"):
            filenames.add(filename)
#except FileNotFoundError:
#    print("Script must be run in directory with access log")



for filename in sorted(filenames, key=str.lower):
    print(filename)


