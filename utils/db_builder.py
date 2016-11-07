import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

#f="data/dumbbell.db"

#################################################################################################
def users():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS users (author TEXT, password TEXT)"
    c.execute(q)    #run SQL query
    db.commit()
    

##################################################################################################
def all_story():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS all_story (story_id INTEGER, title TEXT, terminated BOOLEAN)"
    c.execute(q)
    db.commit()

    
##################################################################################################
def story():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS story (story_id INTEGER, author TEXT, content TEXT)"
    c.execute(q)
    db.commit()
    

##################################################################################################

def check(username):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT author FROM users"
    d = c.execute(q)
    for n in d:
        if(n[0] == username):
            return True
    db.close()
    return False



#True: has not contributed & story open, False: has already contributed or story closed
def check_cont(story_id,username): #checks if user already contributed to a particular story
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT author FROM story WHERE story_id="+str(story_id)
    d = c.execute(q)
    for n in d:
        if(n[0] == username):
            return False
    c = db.cursor()
    q = "SELECT story_id FROM all_story WHERE terminated=0"
    d = c.execute(q)
    for n in d:
        if(n[0] == story_id):
            return True
    db.close()
    return False


# return dict of {title:story_ids} that a user can still contribute to
def open_stories(username):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #q = "SELECT story.story_id, title FROM all_story, story WHERE story.story_id = all_story.story_id"
    q = "SELECT story_id, title FROM all_story"#, story WHERE story.story_id = all_story.story_id"
    m = c.execute(q)
    d = {}
    for n in m:
        if(check_cont(n[0],username)):
            d[n[1]] = n[0]
    return d



# ret True if successfully added, False if username already exists
def add_user(author,password):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    if(not check(author)):
        c = db.cursor()
        q = "INSERT INTO users VALUES ('"+author+"','"+password+"');" #(author,password) VALUES('"+author+"','"+password+"')"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False



def new_story(story_id,title,author,content):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    terminated = 0
    c = db.cursor()
    q = "INSERT INTO all_story VALUES("+str(story_id)+",'"+title+"',"+str(terminated)+")"
    c.execute(q)
    db.commit()
    c = db.cursor()
    q = "INSERT INTO story (story_id,author,content) VALUES(%s,'%s','%s')"%(str(story_id),author,content)
    c.execute(q)
    db.commit()
    db.close()


    
def add_to_story(story_id,author,content):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "INSERT INTO story (story_id,author,content) VALUES(%s,'%s','%s')"%(str(story_id),author,content)
    c.execute(q)
    db.commit()
    db.close()



# 0 = false, 1 = true
def get_story():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT * FROM all_story"
    d = c.execute(q)
    a = []
    for n in d:
        a.append(n)
    db.close()
    return a
  


def get_hash(username):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM users")
    for a in m:
        if a[0]==username:
            db.close()
            return a[1]
    else:
        db.close()
        return None



def get_mystory(username):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #m = c.execute("SELECT all_story.story_id, story.story_id FROM all_story,story WHERE author="+username)
    m = c.execute("SELECT story_id FROM story WHERE author='"+username+"'")
    a = []
    for n in m:
        a.append(n[0])
    db.close()
    return a



def get_title(story_id):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT story_id,title FROM all_story")
    for n in m:
        if (n[0]==story_id):
            db.close()
            return n[1]
    db.close()
    return False



def get_update(story_id):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT story_id,author,content FROM story")
    k = ""
    for n in m:
        if (n[0]==story_id):
             k = n[2]+"\n by "+n[1]
    db.close()
    return k



def get_author(story_id):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT story_id, author FROM story")
    for n in m:
        if (n[0]==story_id):
            return n[1]
    return 0


#returns a list of the contents of a story [[content,author],[content,author],...]
def get_contents(story_id):
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT author,content FROM story WHERE story_id="+str(story_id))
    d = []
    for n in m:
        a.append([n[1],n[0]])
    return d



##################################################################################################

def go():
    users()
    all_story()
    story()

#go()

def close():
    f = "data/dumbbell.db"
    db = sqlite3.connect(f)
    db.commit() #save changes
    db.close()  #close database

    
close()

