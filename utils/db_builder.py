import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="dumbbell.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
#c = db.cursor()    #facilitate db ops

#################################################################################################
def users():
    #make table the first
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS USERS (author TEXT, password TEXT)"
    c.execute(q)    #run SQL query
    #d = c.fetchall()
    

##################################################################################################
def all_story():
    #make table the second
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS ALL_STORY (story_id INTEGER, title TEXT, terminated BOOLEAN)"
    c.execute(q)
    #d = c.fetchall()

    
##################################################################################################
def story():    
    #make yet another table
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS STORY (story_id INTEGER, author TEXT, content TEXT)"
    c.execute(q)
    #d = c.fetchall()
    

##################################################################################################

#get wanted info
#q = "SELECT ALL_STORY.story_id, STORY.story_id FROM ALL_STORY,STORY WHERE ALL_STORY.story_id=STORY.story_id"

#sel = c.execute(q)    #run SQL query
#go()

def add_user(author,password):
    c = db.cursor()
    q = "INSERT INTO USERS VALUES("+author+","+password+")"
    c.execute(q)

def add_new_story(story_id,title,author,content):
    terminated = 0
    c = db.cursor()
    q = "INSERT INTO ALL_STORY VALUES("+story_id+","+title+","+terminated+")"
    c.execute(q)
    c = db.cursor()
    q = "INSERT INTO STORY VALUES('%s','%s','%s')"%(story_id,author,content)
    c.execute(q)

# 0 = false, 1 = true
def get_prompts():
    #q = "SELECT story_id FROM ALL_STORY WHERE terminated=0"
    #c.execute(q)
    c = db.cursor()
    q = "SELECT * FROM ALL_STORY"
    c.execute(q)
    d = c.fetchall()
    for n in d:
        return n
  
#print get_prompts()

def get_hash(username):
    if check(username):
        return USERS[username]
    else:
        return None

##################################################################################################
def close():
    db.commit() #save changes
    db.close()  #close database



def go():
    users()
    all_story()
    story()
    close()

go()



###########
#TODO LIST
# put everything into fxns
# divide information pieces to feed into app.py
# get_hash(username)
# check(username) in db
