from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.lvvxy96.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

application = app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/smj')
def smj():
    return render_template('smj.html')

@app.route('/ksh')
def ksh():
    return render_template('ksh.html')

@app.route('/wjj')
def wjj():
    return render_template('wjj.html')


@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.guest.insert_one(doc)
    
    return jsonify({'msg': '저장 완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.guest.find({},{'_id':False}))
    return jsonify({'result': all_comments})


if __name__ == '__main__':
    app.run()
    
