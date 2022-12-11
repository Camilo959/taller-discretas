from Lectura import *
from Limpiar import *
from Convertir import *
from tkinter import *
from tkinter import filedialog

class Gui:
    def __init__(self):
        self.contenido = ""


    def inicar_ventana(self):
        self.ventana = Tk()
        self.ventana.geometry("350x120")
        self.ventana.title("Grafos")
        self.iniciar_Componentes()
        self.ventana.mainloop()

    def iniciar_Componentes(self):
        self.lbl_title = Label(self.ventana, text="Inserte la ruta del archivo")
        self.font_title = ("Arial", 15, "bold")
        self.lbl_title.configure(font=self.font_title)
        self.lbl_title.place(x=11, y=15, height=20, width=200)

        self.entry_ruta = Entry(self.ventana)
        self.entry_ruta.place(x=17, y=50, height=25, width=220)

        self.btn_send = Button(self.ventana, text="Buscar", command=self.buscar_archivo)
        self.btn_send.place(x=250, y=45, height=28, width=80)

        self.btn_directory = Button(self.ventana, text="Enviar")
        self.btn_directory.place(x=250,y=80, height=28, width=80)

    def buscar_archivo(self):
        ruta = filedialog.askopenfilename(initialdir="Grafos",title="Select",filetypes = (
            ("text files", "*.txt"),
            ("All files", "*.*")))

        objLectura = Lectura()
        self.contenido = objLectura.read(ruta)
        self.control()
        self.mostrar_grafo()


    def mostrar_grafo(self):
        self.gui2 = Tk()
        self.gui2.title("Mostrando")
        self.gui2.geometry("500x500")
        self.inicar_Componentes_gui2()
        self.gui2.mainloop()

    def inicar_Componentes_gui2(self):
        self.font = ("Arial", 15, "bold")

        self.entry_graph = Entry(self.gui2)
        self.entry_graph.place(x=47, y=20, width=400, height=280)

        self.entry_info = Entry(self.gui2)
        self.entry_info.place(x=47, y=320, width=400, height=45)

        self.btn_MA = Button(self.gui2, text="MA")
        self.btn_MA.place(x=30, y=400, width=100, height=50)
        self.btn_MA.configure(font=self.font)

        self.btn_MI = Button(self.gui2, text="MI")
        self.btn_MI.place(x=195, y=400, width=100, height=50)
        self.btn_MI.configure(font=self.font)

        self.btn_LA = Button(self.gui2, text="LA")
        self.btn_LA.place(x=370, y=400, width=100, height=50)
        self.btn_LA.configure(font=self.font)

    def control(self):
        objLimpiar = Limpiar()
        contenido_limpio = objLimpiar.clean_content(self.contenido)
        type_graph = contenido_limpio[0][0]
        contenido_limpio.pop(0)
        contenido_matriz = objLimpiar.for_matrix(contenido_limpio)
        objConvertir = Convertir(contenido_matriz, type_graph)


        if self.contenido == "Error":
            print("Hubo un error chambon")

        list_graph = ['GDLA', 'GDMA', 'GNLA', 'GNMI', 'GPMA', 'GNMA']

        if type_graph == list_graph[0]:
            print(objConvertir.GDLA_f())
            print('Es un grafo: Dirigido Lista de Adyacencia')
        if type_graph == list_graph[1]:
            print('Es un grafo: Dirigido Matriz de Adyacencia')
        if type_graph == list_graph[2]:
            print('Es un grafo: No Dirigido Lista de Adyacencia')
            print(objConvertir.GDLA_f())
        if type_graph == list_graph[3]:
            print('Es un grafo: No Dirigido Matriz de Incidencia')
        if type_graph == list_graph[4]:
            print('Es un grafo: Ponderado Matriz de Adyacencia')
        if type_graph == list_graph[5]:
            print('Es un grafo: No Dirigido Matriz de Adyacencia')