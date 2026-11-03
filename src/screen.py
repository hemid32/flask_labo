from PIL import ImageGrab
import flask
from io import BytesIO

app = flask.Flask(__name__)


@app.route('/screen.png')
def serve_pil_image():
    img_buffer = BytesIO()
    ImageGrab.grab(bbox=(0, 0, 1050, 600), scale_down=True).save(img_buffer, 'PNG', quality=200 )
    img_buffer.seek(0)
    return flask.send_file(img_buffer, mimetype='image/png')


@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('js', path)


@app.route('/')
def serve_img():
    return flask.render_template('screen.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
