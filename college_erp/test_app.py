from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, College ERP!</h1><p>The server is running correctly.</p>'

@app.route('/test')
def test():
    return render_template('simple_home.html')

if __name__ == '__main__':
    print("=" * 50)
    print("Starting minimal test server...")
    print("Visit http://127.0.0.1:5000/ to confirm the server is running")
    print("=" * 50)
    app.run(debug=True)