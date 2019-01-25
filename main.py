#Import Flask and Imported the render_template method from
#the Flask framework

from flask import Flask, render_template
#Flask  is the prototype used to create instances
#of web application or web application
app = Flask(__name__)

#Add different routes
@app.route('/')
def main():
    #you have to pass in a HTML File
    return render_template('index.html')

@app.route('/about/')
def about():
    #this will take you to the aboutMe Homepage
    return render_template('aboutMe.html')

if __name__ == '__main__':
    #print out Python errors on the web page
    # helping us trace the errors
    app.run(debug=True)
