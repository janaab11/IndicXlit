from ai4bharat.transliteration import xlit_server

DEBUG = False
PORT = 8888

app, engine = xlit_server.get_app()

if DEBUG:
    app.run(debug=DEBUG, use_loader=False, port=PORT)
else:
    from flask_cors import CORS
    cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    print("Starting production server...")
    # Gunicorn will be started from the command line.
    # gunicorn -b 0.0.0.0:8888 main:app
