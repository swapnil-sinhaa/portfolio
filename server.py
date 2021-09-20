from flask import Flask, render_template, url_for,request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

#storing data in a text file
def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

#Storing data in a csv file
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar = '"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return 'Form submitted successfully!'
    if request.method =="POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('./thankyou.html')
        
    else:
        return 'Something went wrong. Try Again !'












# @app.route("/<username>/<int:post_id>")
# def hello_world(username = None, post_id = None):
#     return render_template('index.html',name = username, post_id = post_id)

# @app.route("/blog")
# def aboutme():
#     return render_template('blog.html')


# @app.route("/works.html")
# def works():
#     return render_template('works.html')

