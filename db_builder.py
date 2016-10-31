import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="dumbbell.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#################################################################################################

#make table the first
q = "CREATE TABLE USERS (author TEXT, password TEXT)"
c.execute(q)    #run SQL query

#open csv
fObj = open("users.csv")
#read csv
d=csv.DictReader(fObj)
#add csv into table
for k in d:
    p = "INSERT INTO USERS VALUES('%s',%s)"%(k['author'],k['password'])
    c.execute(p)
    

##################################################################################################

#make table the second
q = "CREATE TABLE ALL_STORY (story_id INTEGER, title TEXT, terminated BOOLEAN)"
c.execute(q)

#open csv the second
fObj = open("all_story.csv")
#read csv
d = csv.DictReader(fObj)

#add csv into table
for k in d:
    p = "INSERT INTO courses VALUES('%s',%s,%s)"%(k['story_id'],k['title'],k['terminated'])
    c.execute(p)

    
##################################################################################################
    
#make yet another table
q = "CREATE TABLE STORY (story_id INTEGER, author TEXT, content TEXT)"
c.execute(q)

#open csv
fObj = open("story.csv")
#read csv
d = csv.DictReader(fObj)

#add csv into table
for k in d:
    p = "INSERT INTO courses VALUES('%s',%s,%s)"%(k['story_id'],k['author'],k['content'])
    c.execute(p)

##################################################################################################

#get wanted info
q = "SELECT ALL_STORY.story_id, STORY.story_id FROM ALL_STORY,STORY WHERE ALL_STORY.story_id=STORY.story_id"

sel = c.execute(q)    #run SQL query




##################################################################################################    
    
db.commit() #save changes
db.close()  #close database


###########
#TODO LIST
# put everything into fxns
# divide information pieces to feed into app.py
