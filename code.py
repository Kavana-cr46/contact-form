from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def form():
    return '''
        <form action="/submit" method="post">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" required></textarea><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    # Use the request object to access the form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Escape the input to prevent XSS
    safe_name = html.escape(name)
    safe_email = html.escape(email)
    safe_message = html.escape(message)

    return render_template_string('''
        <h1>Thank You!</h1>
        <p>Your name: {{name}}</p>
        <p>Your email: {{email}}</p>
        <p>Your message: {{message}}</p>
    ''', name=safe_name, email=safe_email, message=safe_message)

if __name__ == '__main__':
    app.run(debug=True)