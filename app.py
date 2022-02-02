from flask import Flask, render_template, request
import conn

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    conn.cur.execute('SELECT * FROM data_mahasiswa;')
    data = conn.cur.fetchall()
    return render_template('home.html', data=data)

@app.route('/insert', methods=['GET'])
def insert():
    return render_template('insert_data.html')

@app.route('/insert_data', methods=['GET', 'POST'])
def insert_data():
    if request.method == "POST":
        details = request.form
        nim = details['nim']
        nama = details['nama']
        umur = details['umur']
        tempat_lahir = details['tempat_lahir']
        jurusan = details['jurusan']
        conn.cur.execute("INSERT INTO data_mahasiswa(nim, nama, umur, tempat_lahir, jurusan) VALUES (%s, %s, %s, %s, %s)", (nim, nama, umur, tempat_lahir, jurusan))
        conn.conn.commit()
        return 'sukses'
    return render_template('home.html')

@app.route('/update_data/<nim>', methods=['GET', 'PUT'])
def update_data(nim):
    if request.method == "PUT":
        details = request.form
        nama = details['nama']
        umur = details['umur']
        tempat_lahir = details['tempat_lahir']
        jurusan = details['jurusan']
        conn.cur.execute("UPDATE data_mahasiswa SET nama=%s, umur=%s, tempat_lahir=%s, jurusan=%s WHERE nim=%s", (nama, umur, tempat_lahir, jurusan, nim))
        conn.conn.commit()
        return 'sukses'
    return render_template('home.html')

@app.route('/delete_data/<nim>', methods=['GET', 'POST'])
def delete_data(nim):
        conn.cur.execute("DELETE FROM data_mahasiswa WHERE nim=%s", (nim,))
        conn.conn.commit()
        return 'sukses'
       