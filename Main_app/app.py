from applications import app
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')