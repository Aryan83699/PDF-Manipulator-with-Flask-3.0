from flask import Flask ,render_template,request,redirect,url_for,send_file
import os
import func as f
import io


app=Flask(__name__)

app.config['Pdf2.0']='Pdf2.0'


@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='POST':
        action=request.form.get("action")
        if action=='pdf2docx':
          return  redirect(url_for('pdf2docx'))
        elif action=='decrypt':
          return  redirect(url_for('decrypt'))
        elif action=='split':
          return  redirect(url_for('split'))
        elif action=='encrypt':
          return  redirect(url_for('encrypt'))
        elif action=='rotate':
          return  redirect(url_for('rotate'))
        elif action=='delete':
          return  redirect(url_for('delete'))
        elif action=='reverse':
            return redirect(url_for('reverse'))
        elif action=='docx2pdf':
           return redirect(url_for('docx2pdf'))
        else :
           return print("Bye bye")

@app.route('/pdf2docx',methods=['GET','POST'])
def pdf2docx():
    if request.method=='POST':
        file = request.files['drop']
        
        
        if file.filename=='':
         return "No Selected File"
        
        if file:
            filepath=os.path.join(app.config['Pdf2.0'],file.filename)
            file.save(filepath)
            temp=f.p2d(filepath)

            return send_file(temp, as_attachment=True)
        

    return render_template('template.html',value='pdf2docx')

@app.route('/decrypt',methods=['POST','GET'])
def decrypt():
    if request.method=='POST':
        file = request.files['drop']
        value=request.form.get('value')
        
        
        if file.filename=='':
         return "No Selected File"
        
        if file:
            filepath=os.path.join(app.config['Pdf2.0'],file.filename)
            file.save(filepath)
            temp=f.decrypt(filepath,value)

            return send_file(temp, as_attachment=True)
    return render_template('decrypt.html',value='decrypt')

@app.route('/split',methods=['GET','POST'])
def split():
    if request.method=='POST':
        file = request.files['drop']
        
        
        if file.filename=='':
         return "No Selected File"
        
        if file:
            filepath=os.path.join(app.config['Pdf2.0'],file.filename)
            file.save(filepath)
            temp=f.split(filepath)

            return send_file(temp, as_attachment=True)

    return render_template('template.html',value='split')

@app.route('/encrypt',methods=['POST','GET'])
def encrypt():
    if request.method=='POST':
        file = request.files['drop']
        value=request.form.get('value')
        
        
        if file.filename=='':
         return "No Selected File"
        
        if file:
            filepath=os.path.join(app.config['Pdf2.0'],file.filename)
            file.save(filepath)
            temp=f.encrypt(filepath,value)

            return send_file(temp, as_attachment=True)
    return render_template('encrypt.html',value='encrypt')

@app.route('/rotate',methods=['GET','POST'])
def rotate():
    if request.method=='POST':
        file = request.files['drop']
        val=int(request.form.get('value'))
        
        
        if file.filename=='':
         return "No Selected File"
        
        if file:
            filepath=os.path.join(app.config['Pdf2.0'],file.filename)
            file.save(filepath)
            temp=f.rotate(filepath,val)

            return send_file(temp, as_attachment=True)
        

    return render_template('rotate.html',value='rotate')

@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        file = request.files['drop']
        value=int(request.form.get('value'))
        
        
        if file.filename=='':
         return "No Selected File"
        
        if file:
            filepath=os.path.join(app.config['Pdf2.0'],file.filename)
            file.save(filepath)
            temp=f.delete(filepath,value)

            return send_file(temp, as_attachment=True)
    return render_template('delete.html',value='delete')

@app.route('/reverse',methods=['GET','POST'])
def reverse():
    if request.method=='POST':
        file = request.files['drop']
        
        
        if file.filename=='':
         return "No Selected File"
        
        if file:
            filepath=os.path.join(app.config['Pdf2.0'],file.filename)
            file.save(filepath)
            temp=f.reverse(filepath)

            return send_file(temp, as_attachment=True)
    return render_template('template.html',value='reverse')

@app.route('/docx2pdf',methods=['GET','POST'])
def docx2pdf():
    if request.method=='POST':
        file = request.files['drop']
        
        
        if file.filename=='':
            return "No Selected File"
        
        if file:
            filepath=os.path.join(app.config['Pdf2.0'],file.filename)
            file.save(filepath)
            temp=f.d2p(filepath)
            return send_file(temp, as_attachment=True)

    return render_template('template.html',value='docx2pdf')

if __name__=='__main__':
    app.run(debug=True)
    