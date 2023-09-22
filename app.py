from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

# comments/<platform>/<mode live|static>/<key>
# alive.com/youtube/as78a83y87y78ws/timed-comments/
# alive.com/youtube/as78a83y87y78ws/live-comments/
# alive.com/youtube/as78a83y87y78ws/sentient/
# alive.com/youtube/as78a83y87y78ws/word-cloud/