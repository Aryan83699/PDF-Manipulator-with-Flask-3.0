from pdf2docx import Converter
# from docx2pdf import convert
import pikepdf as pk
# import io
import pythoncom
import zipfile
import os

def p2d(file):
    old=str(file)
    new=old.replace('.pdf','.docx')
    cv=Converter(old)
    cv.convert(new)
    cv.close()
    return new

# def d2p(file):
#     pythoncom.CoInitialize()
#     old=str(file)
#     # print(file)
#     new=old.replace('.docx','.pdf')
#     convert(old,new)
#     pythoncom.CoUninitialize()
#     return new

def rotate(file,value):
    ol=str(file)
    output='rotated.pdf'
    wk=ol.replace('.pdf','')
    empty=pk.Pdf.new()
    with pk.Pdf.open(file) as f:
        for i in f.pages:   
            page_obj=i     
            current=page_obj.get("/Rotate",0)
            page_obj.Rotate=(current+value)%360
            empty.pages.append(page_obj)
        empty.save('rotated.pdf')
        return output

def split(file):
    old=pk.Pdf.open(file)
    names=[]

    for i,pages in enumerate(old.pages):
        new=pk.Pdf.new()
        name='split'+str(i)+'.pdf'
        new.pages.append(pages)
        new.save(name)
        names.append(name)
    zip_name='splits.zip'
    with zipfile.ZipFile(zip_name,'w') as zipf:
        for name in names:
            zipf.write(name)
    return zip_name


def reverse(file):
    new=pk.Pdf.new()
    f=pk.Pdf.open(file)
    for i in range(len(f.pages)-1,-1,-1):
         p=f.pages[i]
         new.pages.append(p)
         output=os.path.join('Pdf2.0','reversed.pdf')
    new.save(output)
    return output

def delete(file,pageno):
    # pageno=pageno-1
    output='del.pdf'
    new=pk.Pdf.new()
    f=pk.Pdf.open(file)
    for i,j in enumerate(list(f.pages)):
        if i!=pageno-1:
            new.pages.append(j)
    new.save('del.pdf')
    return output


def encrypt(file,password):
    output='encrypt.pdf'
    f=pk.Pdf.open(file)
    no=pk.Permissions(extract=False)

    f.save('encrypt.pdf',encryption=pk.Encryption(user=password,owner='Aryan',allow=no))
    return output


def decrypt(file,password):
    output='decrypt.pdf'
    f=pk.Pdf.open(file,password=password)
    f.save('decrypt.pdf')
    return output


