from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///memo_edit.sqlite"
db = SQLAlchemy(app)

class MemoItem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    body = db.Column(db.Text, nullable = False)

with app.app_context():
    db.create_all()


@app.route('/', methods = ['POST', 'GET'])
def index():
    items = MemoItem.query.order_by(MemoItem.title).all()
    items.insert(0, {'id': 0, 'title': 'CREATE', 'body': ''})
    return render_template('list.html', items = items)

@app.route('/memo/<int:id>', methods = ['GET', 'POST'])
def memo(id):
    it = MemoItem.query.get(id)
    if id == 0 or it is None:
        it = MemoItem(title = 'Untitled', body = '')
    
    if request.method == 'POST':
        it.title = request.form.get('title', 'Untitled')
        it.body = request.form.get('body', '')
        if it.title == '':
            return 'Please enter a title'
        if id == 0:
            db.session.add(it)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('memo.html', it = it)



if __name__ == '__main__':
    app.run(debug = True, port = 8888)

