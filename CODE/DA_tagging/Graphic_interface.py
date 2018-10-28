#!/usr/bin/python
import tkinter
from tkinter import *
from .clusters import *

def fetch(entries):

    metric = ''

    utterance = entries[0]
    method_metric = variable_method.get()
    prantese_position = method_metric.find('(')
    print(prantese_position)

    if prantese_position != -1:
        method =  'Agglomerative' #method_metric[0:prantese_position]
        metric = method_metric[prantese_position+1:-1]

    else:
        method = method_metric

    text_representation_type = variable_text_representation.get()

    DA = entries[3]
    text  = utterance[1].get()

    # methods are Agglomerative and kmeans
    model = cluster(suffixes_extractive_sum, str(method), str(text_representation_type), True, 5, 0.07)
    # metric is euclidean or cosine
    label = model.train(text, metric)

    DA[1].config(text= tag_to_DA[label])

    return

def makeform(root, fields):

    entries = []

    for field in fields:
        row = Frame(root)
        lab = Label(row, width=25, text=field+':', anchor='w')
        lab.pack(side=LEFT)

        if field == 'Utterance':
            ent = Entry(row, width=50)
            ent.pack(side=RIGHT, expand=YES, fill=X)

        if field == 'Method':
            global variable_method
            variable_method = StringVar()
            variable_method.set("kmeans")  # default value
            ent = OptionMenu(row, variable_method, "kmeans", "hierarchical(euclidean)", "hierarchical(cosine)")
            ent.pack()

        if field == "Text Representation":

            global variable_text_representation
            variable_text_representation = StringVar()
            variable_text_representation.set("POS")  # default value
            #lab = Label(row, width=50, text=field, anchor='w')
            ent = OptionMenu(row, variable_text_representation, "POS", "word2vec", "lexical")
            ent.pack()

        if field == "Predicted Dialogue Act":

            #display_text = tkinter.StringVar()
            ent = Label(row, width=50,text="", anchor='w')
            ent.pack(side=RIGHT, expand=YES, fill=X)

        row.pack(side=TOP, fill=X, padx=5, pady=5)
        entries.append((field, ent))

    return entries

def center_window(root):

    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

fields = 'Utterance', 'Method', 'Text Representation', 'Predicted Dialogue Act'

if __name__ == '__main__':

    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    b1 = Button(root, text='Show',command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=10, pady=10)

    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=10, pady=10)

    center_window(root)

    root.mainloop()
