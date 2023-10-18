import os #import os untuk mengakses sistem database

from cs50 import SQL #import SQL untuk menggunakan bahasa SQL dalam phyton

from flask import Flask, flash, jsonify, redirect, render_template, request, session #import tools untuk website

app = Flask(__name__) #mengatur nama aplikasi

db = SQL ("sqlite:///score.db")




@app.route("/", methods=["GET", "POST"])
#ketika route "/" dipanggil/diakses, maka fungsi inde() dieksekusi
def score():
    #jika requst yang dilakukan oleh pungguna adalah post, maka eksekusi kode dalam if 
    if request.method == "POST":
        #access form data / membaca data pada yang diisikan pada form 
        name = request.form.get("name")
        score = request.form.get("score")
        
        # print(name)
        # print(score)
        #masukkan data ke database
        db.execute("INSERT INTO score (name, score) VALUES(?, ?)", name, score)
        # score_test = db.execute("select * from score")
        # print(score_test)

        #balik ke https://127.0.0.1:5000/
        return redirect("/")
        
    # jika requestnya selain post, maka tampilkan data dari tabel birthdays  
    else:
        # ambil seluruh data dari tabel birthdays, simpan di variabel birthdays
        score = db.execute("SELECT * FROM score")

        # salin isi variabel birtdays ke birhdays, lalu kirim ke index.html
        return render_template("index.html", students = score) 


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_data(id):
    if request.method == "GET":
        edt = db.execute("SELECT * FROM score WHERE id = ?", id)[0]
        print(edt)
        return render_template("edit.html", edt = edt)

    elif request.method == "POST":
        edt_name = request.form.get("name")
        edt_score = request.form.get("score")
        db.execute('UPDATE score set name = ?, score = ? where id = ?', edt_name, edt_score, id)
        return redirect("/") 

@app.route("/delete/<id>", methods=["GET"])
def delete(id):
    db.execute("delete from score WHERE id = ?", id)
    return redirect("/")