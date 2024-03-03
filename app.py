from flask import Flask, render_template,request,redirect, flash
import pathlib,csv



app = Flask(__name__)
app.secret_key = b'a secret key'

des = pathlib.Path('templates')
files= list(des.glob('*.html'))


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        file = database.write(f'\n{email}, {name}, {message}')
        
def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"',lineterminator='\n', quoting=csv.QUOTE_MINIMAL,)
        csv_writer.writerow([name,email,message])

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        flash('You have successfully submitted!','success')
        return redirect('index.html')
    else:
        flash('Something went wrong. Pleas try again.', 'error')
        return redirect('index.html')
    
        
        


