from website import create_app

app = create_app()

if __name__ == '__main__':  #Only execute when you actually run it, otherwise it will run instantly
    app.run(debug=True)     #run the app with debug mode
