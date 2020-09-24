Week 4: Many-to-Many Relationships in SQL

#Assignment: A Python program to build a set of tables using the Many-to-Many approach
#to store enrollment and role data.

#This application will read roster data in JSON format, parse the file,
#and then produce an SQLite database that contains a User, Course, and Member table
#and populate the tables from the data file.



import json
import sqlite3

#PART 1: CREATING THE DATABASE

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')
#PART 2: DESERIALIZING THE DATA
#The JSON data we're going to process is stored in an array form, with each
#item being also an array of three elements: one corresponding to the username
#one corresponding to the course name, and one indicating if the user is instructor
#None of them has any field title

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

#PART 3: INSERTING DATA

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry [2];   #Change 1 made to sample code

    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',  #Chane 2 made to sample code
        ( user_id, course_id, role ) )

    conn.commit()


#PART 4: Testing and obtaining the results
test_statement = """
SELECT hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
"""
cur.execute(test_statement)
result = cur.fetchone()
print("RESULT: " + str(result))

#Closing the connection
cur.close()
conn.close()
