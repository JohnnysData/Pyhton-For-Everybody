
CHAPTER 6. STRINGS

6.5. Write code using find() and string slicing (see section 6.10) to extract
the number at the end of the line below.Convert the extracted value to a
floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")
#print(pos)
num = text[pos+5:]
#print(num)
value = float(num)
print(value)

************************************************
#Alternative

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')  #Can also look for '0'
num=text[pos:]
value=float(num)
print(value)

#################################################################################
Chapter 7: FILES

7.1 Write a program that prompts for a file name, then opens that file and reads
through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.

fname = input("Enter file name: ")
fhand = open(fname)
#inp = fhand.read()
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)


***************************************************
# Alternative

fname = input("Enter file name: ")
fhand = open(fname)
#inp = fhand.read()
for line in fhand:
    line = line.rstrip().upper()
    print(line)

***************************************************
#Alternative

for line in fhand:
   print line.upper().strip()

#for line in fhand:
   #line = line.rstrip()
   #print (line.upper())  # upper = method

#################################################################################
7.2. Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter file name: ")
fhand = open(fname)
count = 0
tot = 0
#avg = 0
for line in fhand:

    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    num = line.find (":")
    value = float(line[num+1:])    #pos = line[num+1:]
    tot = tot + value              #value = float(pos)
    avg = tot/count

print("Average spam confidence:", avg)

#Lines after continue are to be indented to the level of "if".
#If there are indented under continue, Python ignores them because
#continue says go back to the top of the program and look for the next thing.

########################################################################################

CHAPTER: 8. LISTS

8.4. Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip()
    words = line.split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)

lst.sort()
print(lst)

##############################################################################################
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'

fname = input("Enter file name: ")

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue

    words = line.split()
    print (words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")


********************************************************************
#Alternative

fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    if line == "": continue

    words = line.split()
    if words[0] !="From": continue

    print(words[1])
    count = count+1

print ("There were", count, "lines in the file with From as the first word")



###########################################################################

CHAPTER: 9: DICTIONARIES

9.4 Write a program to read through the mbox-short.txt and figure out
who has sent the greatest number of mail messages. The program looks for
'From ' lines and takes the second word of those lines as the person who
sent the mail. The program creates a Python dictionary that maps the
sender's mail address to a count of the number of times they appear in
the file. After the dictionary is produced, the program reads through the
dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)

di = dict()
for line in fhand:

    if not line.startswith("From"): continue
    line = line.rstrip()
    words = line.split()
    #email = words[1]
    #print(email)

    for word in email:     # Mistake heppened here. No need of looping over the email to insert it into the dictionary
        di [word] = di.get(word, 0) + 1
        #print(word, di[word])

#print(di)

#Now we want to find the most common word

largest = None
freqword = None

for key, value in di.items():
    if value > largest:
        largest = value
        freqword = key

print(freqword, largest)

******************************************************
# Correct method

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)

di = dict()
for line in fhand:
    if not line.startswith("From "): continue
    line = line.rstrip()
    words = line.split()
    email = words [1]
    #print(email)

    #for word in email:
    di [email] = di.get(email, 0) + 1   #di [words [1]] = di.get(words [1], 0) + 1
         #print(word, di[word])

#print(di)

#Now we want to find the most common word

largest = None
freqword = None

for key, value in di.items():
    if value > largest:
        largest = value
        freqword = key

print(freqword, largest)

*****************************************
#Alternative is remove 'email' and change 'words' to 'words[1]' while inserting 'words' into dictionary.

for line in fhand:

    if not line.startswith("From "): continue
    line = line.rstrip()
    words = line.split()
    #email = words [1]
    #print(email)

    di [words [1]] = di.get(words [1], 0) + 1
         #print(word, di[word])


##########################################################################################
CHAPTER: 10. TUPLES

10.2. Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the
time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.



name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

fhand = open(name)

di = dict()
for line in fhand:
    if not line.startswith("From "): continue
    words = line.split()
    hours = words[5].split(":")
    hours = hours[0]                   #hours=hours[0:2]
    #print (hours)

    #for hours in words:  # Required only when whole file has to checked. Here we are checking only sentnces that start with "From"
    di[hours] = di.get (hours,0) + 1


#print(di)

lst = list()
for key, val in di.items():
    #newtuple = (key,val)
    lst.append((key,val))
    #print(lst)

lst = sorted(lst)
#print(lst)

for key, val in lst:       #for k, v in sorted(counts.items()):
    print(key, val)
