from flask import Flask,jsonify,json,make_response,request,redirect, url_for,abort,render_template
import requests

app=Flask(__name__)

#------------------------------TASK 1-------------------------------------
#main page or index
@app.route('/')
def index():
    return 'HelloWorld - Rohan' #return simple string



#------------------------------TASK 2-------------------------------------
@app.route('/authors')
def hi():

    #---------------------TASK 2a--------------------
    #make request to url
    resForAuthor = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert json to array(javascript object)
    objForAuthor = resForAuthor.json()
    #finding length of array
    lengthOfAuthors=len(objForAuthor)



    #---------------------TASK 2b--------------------
    #make request to url
    resForPost=requests.get('https://jsonplaceholder.typicode.com/posts')
    #convert json to array(javascript object)    
    objForPost=resForPost.json()
    #finding length of array
    lengthOfPosts=len(objForPost)
    
    

    #---------------------TASK 2c--------------------
    post="Author Name : Number Of Posts</br>"
    #iternate over every author
    for i in range(lengthOfAuthors):
        x=0
        post+=objForAuthor[i]["name"]+' : '
        #iterate over every post 
        for j in range(lengthOfPosts):
            #check if a post is wirtten by a specific author(id)
            if objForAuthor[i]["id"]==objForPost[j]["userId"]:
                x=x+1
        post+=str(x)+'</br>'
    return(post)



#------------------------------TASK 3-------------------------------------
@app.route('/setcookie')
def setcookie():
    #getting reasponse from client by sending string to a client
    resp = make_response('cookie is set for name and age')
    #set cookie corresponding to name
    resp.set_cookie('name', 'rohan')
    #set cookie corresponding to age
    resp.set_cookie('age', '22')
    return resp





#------------------------------TASK 4-------------------------------------
@app.route('/getcookies')
def getcookie():
    #if cookie is pesent then retrieve cookie from their key
    cookie=request.cookies.get('name') + '</br>' + request.cookies.get('age')
    return cookie



#------------------------------TASK 5-------------------------------------
@app.route('/robots.txt')
def deny():
    #sending unauthorize acess to client 
    abort(401)
    return 'You donot have enough privilidge'



#------------------------------TASK 6-------------------------------------
@app.route('/html')
def image():
    #sending html string pesent  /templates/main.html file to client
    return render_template('main.html')



#------------------------------TASK 7-------------------------------------
@app.route('/input')
def input():
    #sending input.html string to client
    return render_template('input.html')


@app.route('/getinput', methods=['GET','Post'])
def getinput():
    #check if request is dony POST method
    if request.method=='POST':
        #log the text written in input box
        print(request.form['textbox'])
    #redirect to /input page
    return redirect(url_for('input'))


    

if __name__=="__main__":
    app.run(debug=True)





