import json,re,platform,os,sys
os.system('cls' if platform.system() == 'Windows' else 'clear')
try: 
    import requests
except:
    os.system('pip install requests')
    os.system('cls' if platform.system() == 'Windows' else 'clear')
import requests    
try:
    from flask import *
except:
    os.system('pip install Flask')
    os.system('cls' if platform.system() == 'Windows' else 'clear')
from flask import *

app = Flask(__name__)
@app.route('/apireac_cmt',methods=['GET'])
def test():
    cookie = str(request.args.get('cookie'))
    idcmt = str(request.args.get('idpost'))
    type = str(request.args.get('type'))
    number = 0 if type == 'LIKE' else 1 if type == 'LOVE' else 2 if type == 'CARE' else 3 if type == 'HAHA' else 4 if type == 'WOW' else 5 if type == 'SAD' else 6
    url = 'https://mbasic.facebook.com/reactions/picker/?ft_id='+idcmt
    a = requests.get(url,headers={'cookie':cookie}).text
    b = re.findall('/ufi/reaction/?.*?"',a)
    c = str(b).split('href="')[0].split(',')
    d = c[number].replace('amp;','').replace('"','').split("'")[1]
    link = 'https://mbasic.facebook.com'+str(d)
    done = requests.get(link,headers={'cookie':cookie}).text
    if "Cảnh báo" in done or "Giờ bạn chưa dùng được tính năng này" in done:
        data = {'status':'block','mess':'Thả cảm xúc thất bại'}
        json_dump = json.dumps(data)
        return json_dump
    else:
        data = {'status':'success','mess':'Thả cảm xúc thành công'}
        json_dump = json.dumps(data)
        return json_dump

# done = requests.get(f'http://nlamm.pythonanywhere.com/apireac_cmt?cookie={ck}&idpost={idpost}&type={type}').json()