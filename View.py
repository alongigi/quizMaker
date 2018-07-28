from tkinter import *
from tkinter.ttk import Treeview, Progressbar


class View:
    def __init__(self, controller):
        self.controller = controller
        #self.controller.set_observer(self)
        self.root = Tk()
        self.root.title("Quiz Maker By: Alon Gigi")
        self.docs_entry = Entry(self.root)
        self.docs_entry['width'] = 50
        self.to_stem = False
        self.to_sum = False
        self.to_expand = False
        self.extension_checkbutton = Checkbutton(self.root, text="Extension of query")
        self.summarize_checkbutton = Checkbutton(self.root, text="Summarize document")
        self.progress_bar = Progressbar(self.root, orient=HORIZONTAL, length=200, mode='determinate')
        self.start_btn = Button(text="Start", fg="blue")
        self.run_query = Button(text="Run", fg="blue")
        self.reset_btn = Button(text="Reset process", fg="red")
        self.dictionary_btn = Button(text="Show dictionary", fg="red")
        self.save_btn = Button(text="Save dictionary")
        self.upload_btn = Button(text="Upload dictionary")
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
        docs_btn = Button(self.root, text="browse", command=self.get_path())
        doc_label.grid(row=1, sticky=E)
        self.docs_entry.grid(row=1, column=1)
        docs_btn.grid(row=1, column=2)
        self.start_btn.grid(row=5, column=1)
        self.reset_btn.grid(row=6, column=0)
        self.reset_btn['state'] = 'disabled'
        self.dictionary_btn.grid(row=6, column=2)
        self.save_btn.grid(row=7, column=1)
        self.upload_btn.grid(row=7, column=2)
        self.status_bar.grid(row=8, column=0, columnspan=3, sticky=W)
        self.progress_bar.grid(row=9, column=0, columnspan=3, sticky=(W, E))

    def get_path(self):
        pass
        file_path = filedialog.askdirectory()
        self.controller.doc_path = file_path
        self.docs_entry.delete(0, len(self.docs_entry.get()))
        self.docs_entry.insert(0, file_path)


