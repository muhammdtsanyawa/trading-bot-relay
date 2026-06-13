import os,json,requests
from flask import Flask,request,jsonify
app=Flask(__name__)
TOKEN="8235561935:AAGOY_jlJxvBGbAWPF6p94qHK9eyg1bAvH0"
CHAT="7974666080"
URL=f"https://api.telegram.org/bot{TOKEN}/sendMessage"
@app.route("/webhook",methods=["POST"])
def webhook():
    d=json.loads(request.get_data(as_text=True))
    t=d.get("type","?")
    e="🟢 LONG" if t=="LONG" else "🔴 SHORT"
    msg=(f"*{e} - {d.get('symbol','?')}*\n"
         f"📍 Entry: `{d.get('entry','?')}`\n"
         f"🎯 TP: `{d.get('tp','?')}`\n"
         f"🛑 SL: `{d.get('sl','?')}`\n"
         f"⚖️ RR: `1:{d.get('rr','?')}`\n"
         f"🔥 ADX: `{d.get('adx','?')}`\n"
         f"⏱ TF: `{d.get('tf','?')}`")
    requests.post(URL,json={"chat_id":CHAT,"text":msg,"parse_mode":"Markdown"})
    return jsonify({"status":"ok"})
@app.route("/health")
def health():
    return "ok"
if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.getenv("PORT",5000)))
