from app.application import Application

if __name__ == "__main__":
    app = Application()
    try:
        app.run()
    except KeyboardInterrupt:
        quit()
