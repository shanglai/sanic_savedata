"""
App simple que toma datos por POST y los guarda en un archivo.
El archivo esta definido en un path con:
request_<ip>_<timestamp>_<hexadecimal_random>.
DALN
"""

from sanic import Sanic,response
from sanic.response import json,text
import re,random
from socket import gethostname,gethostbyname
from datetime import datetime

path='/home/kirito/scripts/sanic_data'

app= Sanic('string-saver')

@app.route('/save',methods=['POST'])
async def on_post(request):
  ip= re.sub('[.-]','_',gethostname().split('.')[0])
  ts= datetime.now().strftime('%Y%m%d%H%M%S%f')
  rhash= hex(random.getrandbits(128))[2:-1]
  fname= '{}/request_{}_{}_{}'.format(path,ip,ts,rhash)
  #print('Hola OK')
  #print(request)
  print(request.body)
  #print(request.json)
  #print(request.args)
  #print(request.query_args)
  #print(request.query_string)
  #print(request.ctx)
  #return json({'hello':'world'})
  #return response.text('hola desde Sanic!\n')
  print(fname)
  with open(fname,'w') as outfile:
    outfile.write('{}\n'.format(request.body))
  return json({'status':200})

if __name__=='__main__':
  app.run(host='0.0.0.0',port=8000,debug=True)

