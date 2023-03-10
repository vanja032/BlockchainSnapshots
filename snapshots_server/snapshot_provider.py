import subprocess
import json
import time
from datetime import datetime
import os
import shutil
import threading
from waitress import serve
from flask import *
from flask_cors import CORS, cross_origin

file = open('config.json')
configs = json.loads(file.read())
file.close()

snap_location = configs['snapshot_path']
snap_dir = configs['snap_dir']
snapshot = ""
#snap_file = configs['snapshot_file']
#snap_file_ext = configs['snapshot_file_extension']
webpage_address = configs['snapshot_webpage']

favicon = 'favicon.png'
#file_name_ext = ""

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
#@cross_origin()
def ProvideSnapshot():
    try:
        #global file_name_ext
        global snapshot
        #return render_template('index.html', snapshot_file_download = '/snapshot', snapshot_url = f'--no-check-certificate {webpage_address}/snapshot -o', snapshot_out = f'{snap_file}_{file_name_ext}{snap_file_ext}', favicon_url = f'/{favicon}')
        return render_template('index.html', snapshot_file_download = '/snapshot', command = 'curl -k', snapshot_url = f'{webpage_address}/snapshot -o', snapshot_out = f'{snapshot}', favicon_url = f'/{favicon}')
        #return "<h1>Hello!</h1>"
    except Exception as ex:
        print(ex)

@app.route('/snapshot', methods=['GET'])
#@cross_origin()
def DownloadSnapshot():
    try:
        #global file_name_ext
        global snapshot
        with open(f'{snap_dir}/{snapshot}') as file:
            file.seek(0)
            return send_file(file.name, as_attachment=True)
        #return send_file(f'{snap_dir}/{snap_file}_{file_name_ext}{snap_file_ext}', as_attachment=True)
        #return send_file(f'{snap_dir}/{snapshot}', as_attachment=True)
    except Exception as ex:
        print(ex)

@app.route(f'/version', methods=['GET'])
#@cross_origin()
def ReturnSnapshotVersion():
    try:
        #global file_name_ext
        global snapshot
        #return f'{snap_file}_{file_name_ext}{snap_file_ext}'
        return f'{snapshot}'
    except Exception as ex:
        print(ex)

@app.route(f'/{favicon}', methods=['GET'])
#@cross_origin()
def ReturnFavicon():
    try:
        global favicon
        return send_file(f'{favicon}', as_attachment=True)
    except Exception as ex:
        print(ex)

def ExportSnapshot():
    try:
        #global file_name_ext
        global snapshot
        print("\nExporting snapshot...\n" + str(datetime.now()))
        os.system('rm -rf ' + snap_location + '/*')
        command = 'curl -X POST http://127.0.0.1:8888/v1/producer/create_snapshot'
        subprocess.run(command, shell=True, capture_output=False)
        file_name_ext = str(time.time())
        time.sleep(2)
        os.system('rm -rf ' + snap_dir + '/*')
        #shutil.copy(snap_location + '/' + os.listdir(snap_location)[0], f'{snap_dir}/{snap_file}_{file_name_ext}{snap_file_ext}')
        snapshot = os.listdir(snap_location)[0]
        shutil.copy(snap_location + '/' + snapshot, f'{snap_dir}/{snapshot}')
        print("\nExporting snapshot finished.\n" + str(datetime.now()))
        #time.sleep(600) # every 10 minutes export a snapshot
    except Exception as ex:
        print(ex)
    #ExportSnapshot()
   
def CallExport():
    while True:
        try:
            ExportSnapshot()
            time.sleep(600) # Every 10 minutes export 60s * 10mins
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    try:
        #app.run(host='0.0.0.0', port=80)
        thread = threading.Thread(target=CallExport, name="Exporting snapshots")
        thread.setDaemon(True) # Stop this thread if the main thread is stopped
        thread.start()
        #serve(app, host="0.0.0.0", port=443, url_scheme='https')
        app.run(host='0.0.0.0', port=443, ssl_context=("<path to the certificate>/cert.pem", "<path to the certificate>/privkey.pem"), threaded=True)
    except Exception as ex:
        print(ex)
