from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Film verisi burada tutulacak (normalde bir veritabanına bağlanılır)
movies = []

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:id>')
def movie_detail(id):
    movie = movies[id]
    return render_template('movie-detail.html', movie=movie)

@app.route('/admin')
def admin():
    return render_template('admin.html', movies=movies)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        movie = {
            'title': request.form['movie-title'],
            'poster': request.files['movie-poster'],
            'description': request.form['movie-description'],
            'actors': request.form['movie-actors'],
            'trailer': request.form['movie-trailer']
        }
        movies.append(movie)
        return redirect('/admin')
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
