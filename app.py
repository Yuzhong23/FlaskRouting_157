from flask import Flask, render_template, request, redirect, url_for  # Mengimpor modul Flask dan fungsi terkait

app = Flask(__name__)  # Membuat instance aplikasi Flask

@app.route('/')  # Mendefinisikan route untuk halaman login
def login():
    return render_template('login.html')  # Merender template login.html

@app.route('/home', methods=['POST'])  # Mendefinisikan route untuk halaman home, hanya menerima metode POST
def home():
    name = request.form.get('name')  # Mengambil nama dari form
    return render_template('home.html', name=name)  # Merender template home.html dengan nama yang diteruskan

@app.route('/back', methods=['GET'])  # Mendefinisikan route untuk tombol kembali
def back_to_login():
    return redirect(url_for('login'))  # Mengarahkan kembali ke halaman login

if __name__ == 'main':  # Memulai aplikasi jika dijalankan langsung (seharusnya '_main_')
    app.run(debug=True)  # Menjalankan aplikasi dalam mode debug