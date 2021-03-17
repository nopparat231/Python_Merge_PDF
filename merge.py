import os
import tempfile
import PyPDF2
from pdf2image import convert_from_path
from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


master = Tk() 
master.title('Merge PDF')
master.geometry('530x125') 
folder_pathin1 = StringVar()
folder_pathin2 = StringVar()
folder_pathout = StringVar()

def browse_buttonin1():
    global folder_pathin1
    filename1 = filedialog.askopenfile(mode ='r', filetypes =[("PDF files", "*.pdf")])
    folder_pathin1.set(filename1.name)
    lbl1.configure(text=folder_pathin1)

def browse_buttonin2():
    global folder_pathin2
    filename2 = filedialog.askopenfile(filetypes=[("PDF files", "*.pdf")])
    folder_pathin2.set(filename2.name)
    lbl2.configure(text=folder_pathin2)


def browse_buttonout():
    global folder_pathout
    filename = filedialog.askdirectory()
    folder_pathout.set(filename)
    lbl3.configure(text=folder_pathout)


# Crop img
def mgpdf(inputf1,inputf2,outpf):
    pdf_first = open(inputf1,'rb') 
    pdf_second = open(inputf2,'rb')
    reader_first = PyPDF2.PdfFileReader(pdf_first)
    reader_second = PyPDF2.PdfFileReader(pdf_second)
    writer = PyPDF2.PdfFileWriter()
    for pageNum in range(reader_first.numPages):
        page = reader_first.getPage(pageNum)
        writer.addPage(page)
    for pageNum in range(reader_second.numPages):
        page = reader_second.getPage(pageNum)
        writer.addPage(page)
    outputfile = open(outpf + '/' + (os.path.splitext(os.path.basename(inputf1))[0]) + '_merge.pdf','wb')
    writer.write(outputfile)
    outputfile.close()
    pdf_first.close()
    pdf_second.close()

#run Funtion

def connv():
    inputf1 = lbl1.get()
    inputf2 = lbl2.get()
    outpf = lbl3.get()
    try:
        mgpdf(inputf1,inputf2,outpf)
    except:
        Result = "NO pdf found"
        messagebox.showerror("Error", Result)
    else:
        Result = "success"
        messagebox.showinfo("success", Result)


#in1
Label(master, text="PDF File1 : ").grid(row=0,sticky=(N, W)) 
#in2
Label(master, text="PDF File2 : ").grid(row=1,sticky=(N, W)) 

#out
Label(master, text="Out File : ").grid(row=2,sticky=(N, W)) 



lbl1 = Entry(master,width=65,state="disabled")
lbl1.grid(row=0, column=1,sticky=(N, W))

button1 = Button(text="Browse", command=browse_buttonin1)
button1.grid(row=0, column=2)

lbl2 = Entry(master,width=65,state="disabled")
lbl2.grid(row=1, column=1,sticky=(N, W))

button2 = Button(text="Browse", command=browse_buttonin2)
button2.grid(row=1, column=2)


lbl3 = Entry(master,width=65,state="disabled")
lbl3.grid(row=2, column=1,sticky=(N, W))

button2 = Button(text="Browse", command=browse_buttonout)
button2.grid(row=2, column=2)

bcon = Button(master, text="Merge", command=connv)
bcon.grid(row=3, column=2)

#out
Label(master, text="@Nopparat-Budd V1.0").grid(row=4, column=1,sticky=(N, W)) 

mainloop()