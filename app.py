from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# ✅ Always initialize DB on import
def init_db():
    conn = sqlite3.connect('dreams.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS dreams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            original TEXT,
            rewritten TEXT,
            style TEXT,
            tags TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    rewritten = ''
    if request.method == 'POST':
        author = request.form['author']
        dream = request.form['dream']
        style = request.form['style']
        tags = request.form['tags']
        rewritten = rewrite_dream(dream, style)
        save_dream(author, dream, rewritten, style, tags)
    return render_template('index.html', rewritten=rewritten)

@app.route('/dreams')
def dreams():
    conn = sqlite3.connect('dreams.db')
    c = conn.cursor()
    c.execute('SELECT * FROM dreams ORDER BY id DESC')
    all_dreams = c.fetchall()
    conn.close()
    return render_template('dreams.html', dreams=all_dreams)

@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        tag = request.form['tag'].strip().lower()
        conn = sqlite3.connect('dreams.db')
        c = conn.cursor()
        c.execute('SELECT * FROM dreams WHERE tags LIKE ?', ('%' + tag + '%',))
        results = c.fetchall()
        conn.close()
    return render_template('search.html', results=results)

def rewrite_dream(text, style):
    if style == 'plain':
        return text
    elif style == 'poetic':
        return f"🌺 ఇది నా కల... {text} 🌺"
    elif style == 'story':
        return f"📖 ఒకప్పుడు కలలో... {text}"
    else:
        return text

def save_dream(author, original, rewritten, style, tags):
    conn = sqlite3.connect('dreams.db')
    c = conn.cursor()
    c.execute('INSERT INTO dreams (author, original, rewritten, style, tags) VALUES (?, ?, ?, ?, ?)',
              (author, original, rewritten, style, tags))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
