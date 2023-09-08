import sys
import flask
import pytoolslib as pt

projPath = "/Users/noahdorfman/Library/Mobile Documents/com~apple~CloudDocs/maker/pyToolsProj"
libPath = projPath + "/pytoolslib"
scriptsPath = projPath + "/testScripts"

sys.path.insert(0, libPath)

manager = pt.manager()
manager.registerModules(scriptsPath)


app = flask.Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/list")
def list():
    return flask.jsonify(scripts.keys())

if __name__ == "__main__":
  app.run()