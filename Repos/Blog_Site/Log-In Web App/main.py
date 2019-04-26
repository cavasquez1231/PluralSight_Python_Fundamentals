from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return """
    
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.btn {
  border: none;
  background-color: inherit;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  display: inline-block;
}

.btn:hover {background: #eee;}

.success {color: green;}
.info {color: dodgerblue;}
.warning {color: orange;}
.danger {color: red;}
.default {color: black;}
</style>
</head>
<body>

                <h1>Click the log-in button below, then scan your QR Code!</br></br></br></br></h1>
                
                <button class="btn success">Log In</button>
                
</body>
</html>

                

                """

@app.route("/about")
def about():
    return "<h1>Help</h1>"

if __name__ == '__main__':
    app.run(debug=True)