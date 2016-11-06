
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


#f="data/dumbbell.db"
#f="../data/dumbbell.db"

#db = sqlite3.connect(f) #open if f exists, otherwise create
#c = db.cursor()    #facilitate db ops

#################################################################################################
def users():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS users (author TEXT, password TEXT)"
    c.execute(q)    #run SQL query
    

##################################################################################################
def all_story():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS all_story (story_id INTEGER, title TEXT, terminated BOOLEAN)"
    c.execute(q)

    
##################################################################################################
def story():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS story (story_id INTEGER, author TEXT, content TEXT)"
    c.execute(q)
    

##################################################################################################

#get wanted info
#q = "SELECT all_story.story_id, story.story_id FROM all_story,story WHERE all_story.story_id=story.story_id"

#sel = c.execute(q)    #run SQL query
#go()


def check(username):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT author FROM users"
    d = c.execute(q)
    #d = c.fetchall()
    for n in d:
        #print n
        if(n == username):
            return True
    return False
check("not")
#print check("nicole")
#print check("test")

# ret True if successfully added, False if username already exists
def add_user(author,password):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    if(not check(author)):
        c = db.cursor()
        q = "INSERT INTO users VALUES ('"+author+"','"+password+"');" #(author,password) VALUES('"+author+"','"+password+"')"
        c.execute(q)
        return True
    else:
        return False
#add_user("nicole","abc")
#add_user("test","abc")
def add_new_story(story_id,title,author,content):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    terminated = 0
    c = db.cursor()
    q = "INSERT INTO all_story VALUES("+str(story_id)+",'"+title+"',"+str(terminated)+")"
    c.execute(q)
    c = db.cursor()
    q = "INSERT INTO story (story_id,author,content) VALUES(%s,'%s','%s')"%(str(story_id),author,content)
    c.execute(q)

#add_new_story(1,"story_title","nicole","this is story content")
'''
c = db.cursor()
q = "SELECT * FROM users"
d = c.fetchall()
for n in d:
    print n
    print "n/a"
'''
    
# 0 = false, 1 = true
def get_prompts():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    #q = "SELECT story_id FROM all_story WHERE terminated=0"
    #c.execute(q)
    c = db.cursor()
    q = "SELECT * FROM all_story"
    d = c.execute(q)
    #d = c.fetchall()
    for n in d:
        return n
  
#print get_prompts()

def get_hash(username):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM users")
    for a in m:
        if a[0]==username:
            return a[1]
    else:
        return None
#print get_hash("nicole")

##################################################################################################

def go():
    users()
    all_story()
    story()
    #close()

#go()

def close():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    db.commit() #save changes
    db.close()  #close database

close()




###########
#TODO LIST
# put everything into fxns
# divide information pieces to feed into app.py
# get_hash(username)
# check(username) in db
