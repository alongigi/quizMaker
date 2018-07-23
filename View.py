from tkinter import *
from tkinter.ttk import Treeview, Progressbar


class View:
    def __init__(self):
        #self.controller = controller
        #self.controller.set_observer(self)
        self.root = Tk()
        self.root.title("Quiz Maker By: Alon Gigi")
        self.docs_entry = Entry(self.root)
        self.docs_entry['width'] = 50
        self.to_stem = False
        self.to_sum = False
        self.to_expand = False
        self.stem_checkbutton = Checkbutton(self.root, text="stemming")
        self.extension_checkbutton = Checkbutton(self.root, text="Extension of query")
        self.summarize_checkbutton = Checkbutton(self.root, text="Summarize document")
        self.progress_bar = Progressbar(self.root, orient=HORIZONTAL, length=200, mode='determinate')
        self.start_btn = Button(text="Start", fg="blue")
        self.run_query = Button(text="Run", fg="blue")
        self.reset_btn = Button(text="Reset process", fg="red")
        self.dictionary_btn = Button(text="Show dictionary", fg="red")
        self.cache_btn = Button(text="Show cache", fg="red")
        self.save_btn = Button(text="Save dictionary and cache")
        self.upload_btn = Button(text="Upload dictionary and cache")
        self.show_summary = Button(text="Show summary")
        self.status_bar = Label(self.root)
        self.status_bar_text = StringVar()
        self.status_bar['textvariable'] = self.status_bar_text
        self.status_bar_text.set('Status:')
        self.summary = {}
        self.create_view()
        self.path_result = []

    def start(self):
        '''
        start the user interface
        '''
        self.root.mainloop()

    def create_view(self):
        '''
        create the view window
        '''
        theme_label = Label(self.root, text="Quiz Maker", bg="blue", fg="white")
        theme_label.grid(row=0, column=1)
        doc_label = Label(self.root, text="File for creating quiz")
        docs_btn = Button(self.root, text="browse")
        doc_label.grid(row=1, sticky=E)
        self.docs_entry.grid(row=1, column=1)
        docs_btn.grid(row=1, column=2)
        self.start_btn.grid(row=5, column=1)
        self.reset_btn.grid(row=6, column=0)
        self.reset_btn['state'] = 'disabled'
        self.cache_btn.grid(row=6, column=1)
        self.dictionary_btn.grid(row=6, column=2)
        self.show_summary.grid(row=7, column=0)
        self.show_summary['state'] = 'disabled'
        self.save_btn.grid(row=7, column=1)
        self.upload_btn.grid(row=7, column=2)
        self.stem_checkbutton.grid(row=5, column=0)
        self.status_bar.grid(row=8, column=0, columnspan=3, sticky=W)
        self.progress_bar.grid(row=9, column=0, columnspan=3, sticky=(W, E))


