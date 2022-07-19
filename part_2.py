from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
import re
import string

# creating root object
root = Tk()

# defining size of window
root.geometry("900x450")

# setting up the title of window
root.title("RESUME SCREENING BASED ON JOB DESCRIPTION")


# ============================================#

# clicked function 1
def clicked1():
    messagebox.showinfo('INFO', 'FILE SELECTED')


# Resume file opening function
def openfile_resume():
    global pdfReader
    path2 = filedialog.askopenfilename()
    pdfFileObj = open(path2,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    clicked1()



# Function to screen resume
def screen():
    count = 0
    text = ""
    num_pages = pdfReader.numPages
    # Extract text from every page on the file
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
    # Convert all strings to lowercase
    text = text.lower()
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Create dictionary with technical key terms by area
    data_set = {
        'Android Developer':['android development','data structures','android',
                             'html','css','c++','java','kotlin','android studio',
                             'xml','sql','android testing','coding','testing','api',
                             'android software development kit','sdk','git','ui',
                             'ux','user interface','eclipse','xamarin','programming',
                             'jsp','oracle','scrum','gradle','json']}
    # Initializie score counters for each area
    Andro_cand = 0
    # Obtain the scores for each area
    for area in data_set.keys():

        if area == 'Android Developer':
            for word in data_set[area]:
                if word in text:
                    Andro_cand += 1
            print("TOTAL KEYWORDS MATCHED :")
            print(Andro_cand)
    #converting required count into integer
    req_key=int(txtkey.get())
    if Andro_cand >= req_key:
        messagebox.showinfo('INFO', 'Candidate selected for interview')
    else:
        messagebox.showinfo('INFO', 'Candidate not selected')
        


# exit function
def qExit():
    root.destroy()


# labels for heading
lblInfo = Label(root, font=('arial', 18, 'bold'),text="RESUME SCREENING For Android Developer",fg="Black", bd=10, anchor='w')
lblInfo.grid(row=1, column=2)

# labels line 1
lblline1 = Label(root, font=('arial', 16, 'bold'),text="==============================", bd=16, anchor="w")
lblline1.grid(row=3, column=2)

# labels for the key entry
lblkey = Label(root, font=('arial', 12, 'bold'),text="CHOOSE THE RESUME", bd=16, anchor="w")
lblkey.grid(row=6, column=1)

# resume button
btnchoose2 = Button(root, padx=16, bd=10, fg="white", font=('arial', 10, 'bold'), width=7, text="CHOOSE", bg="grey",command=openfile_resume)
btnchoose2.grid(row=6, column=2)

# keyword count
lblInfo = Label(root, font=('arial', 12, 'bold'),text=" Keyword Required",fg="Black", bd=16, anchor='w')
lblInfo.grid(row=8, column=1)


# Entry box for the count
txtkey = Entry(root, font=('arial', 16, 'bold'), bd=10, insertwidth=4,
               bg="powder blue", justify='right')
txtkey.grid(row=8, column=2)

# resume button
btnchoose3 = Button(root, padx=16, bd=10, fg="white", font=('arial', 10, 'bold'), width=7, text="SCREEN", bg="grey",command=screen)
btnchoose3.grid(row=9, column=2)

# labels line 2
lblline2 = Label(root, font=('arial', 16, 'bold'),text="==============================", bd=16, anchor="w")
lblline2.grid(row=7, column=2)

# labels for Name
lblname = Label(root, font=('arial', 16, 'bold'),text="Ridhanshu Jasrotia (2017359)", bd=16, anchor="w")
lblname.grid(row=10, column=2)

# Exit button
btnExit = Button(root, padx=16, bd=10, fg="white", font=('arial', 10, 'bold'), width=7, text="Exit", bg="grey",command=qExit)
btnExit.grid(row=9,column=3)

# keeps window alive
root.mainloop()