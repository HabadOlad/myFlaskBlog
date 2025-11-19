#this project uses flask-login,Flask-SQLAlchemy and flask , remember for the requirements txt! 
from website import create_app 

if __name__ == "__main__":
    app = create_app()
    app.run(debug = True)






