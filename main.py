#THIS IS OUR FLASK APP THAT WE CREATE to run to see it on server 

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)