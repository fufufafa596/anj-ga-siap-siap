from flask import Flask

app = Flask(__name__)

@app.route('/')
def gombal():
    return '''
    <html>
      <head><title>Gombalan Spesial</title></head>
      <body style="text-align: center; margin-top: 100px;">
        <h1>Kamu itu kayak charger rusak...</h1>
        <h2>Meski nyambungnya sebentar, aku tetap butuh kamu setiap saat.</h2>
      </body>
    </html>
    '''

# Wajib: handler untuk Vercel
def handler(environ, start_response):
    return app(environ, start_response)
