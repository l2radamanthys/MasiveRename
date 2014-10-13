
import Tkinter as tk
from tkFileDialog import askdirectory
#import tkTreectrl as tkTree
import ttk
import os


class MainFrame(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, master=root, width=400)
        self.pack()

        lbl1 = tk.Label(self, text="Carpeta:")
        lbl1.grid(row=0, padx=5, pady=5, sticky=tk.W)

        self.path = tk.StringVar()
        edt_folder_path = tk.Entry(self, textvariable=self.path, width=80)
        edt_folder_path.grid(row=1, column=0, columnspan=3)
        
        btn_folder = tk.Button(self, text='Seleccionar', command=self.select_folder, pady=5)
        btn_folder.grid(row=1, column=3, padx=5)
        
        lbl4 = tk.Label(self, text="Archivos:")
        lbl4.grid(row=2, padx=5, pady=5, sticky=tk.W)
        
        self.listbox = tk.Listbox(self, width=80)
        #self.listbox = tkTree.MultiListbox(self, width=80)
        #self.listbox.config(columns=('Antes', 'Despues'))
        self.listbox.grid(row=3, column=0, columnspan=3)
        
        self.scroll = tk.Scrollbar(self.listbox, orient=tk.VERTICAL)
        #self.scroll.grid(row=3, column=4)

        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        
        btn_refresh = tk.Button(self, text='Refrescar', command=self.refresh_file_list, pady=5)
        btn_refresh.grid(row=3, column=3, padx=5)
        
        lbl2 = tk.Label(self, text="Buscar:")
        lbl2.grid(row=4, padx=5, pady=5, sticky=tk.W)

        self.search = tk.StringVar()
        edt_search = tk.Entry(self, textvariable=self.search, width=30)
        edt_search.grid(row=4,column=1, columnspan=2, sticky=tk.W)
         
        lbl3 = tk.Label(self, text="Reemplazar:")
        lbl3.grid(row=5, padx=5, pady=5, sticky=tk.W)
    
        self.replace = tk.StringVar()
        edt_replace = tk.Entry(self, textvariable=self.replace, width=30)
        edt_replace.grid(row=5, column=1, columnspan=2, sticky=tk.W)

        btn_action = tk.Button(self, text="Reemplazar", command=self.rename_files, pady=5)
        btn_action.grid(row=6, column=1, sticky=tk.E)
        btn_quit = tk.Button(self, text="Salir", command= self.quit, padx=15, pady=5)
        btn_quit.grid(row=6, column=2, sticky=tk.W)

        #
        self.refresh_file_list()


    def select_folder(self):
        """
        """
        fpath = askdirectory()
        if fpath != None:
            self.path.set(fpath)
 

    def refresh_file_list(self):
        """
        """
        path = self.path.get()
        if path == "":
            path = os.getcwd()
            self.path.set(path)
        #limpiar lista
        self.listbox.delete(0, tk.END)
        #agregar elementos del directorio actual
        for _file in os.listdir(path):
            self.listbox.insert(tk.END, _file)
            #print file

    
    def rename_files(self):
        """
        """
        _search = self.search.get()
        _replace = self.replace.get()
        path = self.path.get()
        if path != None:
            for _file in os.listdir(path):
                nfile = _file.replace(_search, _replace)
                try:
                    os.rename(os.path.join(path, _file), os.path.join(path, nfile))
                except:
                    print "error", nfile
                    pass
            self.refresh_file_list()


def main():
    main = tk.Tk()
    main.title('Renombrador Masivo')
    app = MainFrame(main)
    main.mainloop()



if __name__ == '__main__':
    main()
