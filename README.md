# jubilant-backend
Learning ins and outs of backend development

Okay, I've been interested in backend from long time. Finally learning it. It is so FASCINATING...
I am following some udacity courses.

# 1. Client and Web Server Communication (I'll add notes later)

# 2. HTTP and Web Servers
    - you can find the complete code here -> https://github.com/udacity/course-ud303
    - you write web servers from scratch and know how each component holds together 
    - Hello server (just prints hello when a request is hit)
    - Echo server (little dynamic, prints whatever you pass as query param)
    - MessageBoard server (POST requests, shows all previous messages)
    - BookMark Server(urlShortner, stores all urls with shortnames)
    - JSON
    # Key Points to learn:
      - Headers are important and they vary with kind of requests.
      - You can send html forms as string to display in browser via a request
      - Content-type is set according to what you are gonna send to browser, and getting it wrong throws a TypeError
      - Write good error messages and print statements to understand the flow.
     # Deploying to heroku
     1. create an account on heroku and install heroku cli
     2. put project in a new git folder
     3. create 3 config files:
        #1. runtime.txt tells Heroku what version of Python you want to run.
        #2. requirements.txt is used by Heroku (through pip) to install dependencies of your application that aren't in the Python standard library.
        #3.Procfile is used by Heroku to specify the command line for running your application.
        NOTE: to create a Procfile in windows: echo web: run this thing >Procfile (and later edit it)
     4. configure port to listen from environment variables
     5. heroku create app-name //to create app
     6. git push heroku master ...and voila! You have the url of deployed server
    
