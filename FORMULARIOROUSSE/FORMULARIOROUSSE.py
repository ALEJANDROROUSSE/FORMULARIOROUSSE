import tkinter as tk
from tkinker import messagebox
import re

   def guadar_datos();
    #obtener los datos de los campos 
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    edad= entry_edad.get()
    estatura = entry_estatura.get()
    telefono = entry_telefono.get()
    
    #obtener el género seleccionado
    genero = ""
    if  var_genero.get()==1:
        genero = "Hombre"
    elif var_genero.get()==2 :
        genero= "mujer"
        
    #validar que los campos tengan el formato correcto
    if (es_entero_valido(edad)and es_decimal_valido(estatura) and
        es_entero_valido_de_10_digitos(telefono)and es_texto_valido(nombres)and es_texto_valido(apellidos));
    datos= f"Nombres:{nombres}\nApellidos:{apellidos}\nEdad:{edad} años\nEstatura:{estatura}cm\nTeléfono:{telefono}\nGénero:{genero}"
    #Guardar los datos en un archivo de texto 
    with open ("datos.txt","a")as archivo:
        archivo.write(datos+"\n\n")
        #mostrar un mensaje con los datos capturados
        messagebox.showinfo("inofrmación","Datos guardados con éxito:\n\n"+ datos)
        #Limpiar los controles después de guadar
        limpiar_campos()
    else: messagebox.showerror("Error","por favor,ingrese datos válidos en los campos.")
        
        
        
        
        
        def limpiar_campos ();:
            entry_nombres.delete(0,tk.END)
            apellidos = entry_apellidos.delete(0,tk.END)
            edad= entry_edad.delete(0,tk.END)
            estatura = entry_estatura.delete(0,tk.END)
            telefono = entry_telefono.delete(0,tk.END)
            var_genero.set(0)
            
        def es_entero_valido(valor):
            try:
                int(valor)
                return True
            except ValueError:
                return False
        def es_decimal_valido(valor):
            try:
                float(valor)
                return True
            except ValueError:
                return False
        def es_entero_valido_de_10_digitos(valor):
            return valor.isdigt()and len (valor)== 10 
        
        def es_texto_valido(valor):
            return bool(re.match("^[a-zA-Z\s]+$",valor))
        
        #crear la ventana principal 
        ventana=tk.Tk()
        ventana.title("Formulario")
        
        #crear variables para los RadioButtons
        var_genero= tk.IntVar()
        #crear etiquetas y campos de entrada 
        label_nombres=tk.Label(ventana,text="Nombres:")
        label_nombres.pack()
        entry_nombres=tk.Entry(ventana)
        entry_nombres.pack()
        
        label_apellidos=tk.Label(ventana,text="Apellidos:")
        label_apellidos.pack()
        entry_apellidos=tk.Entry(ventana)
        entry_apellidoss.pack()
        
        label_edad=tk.Label(ventana,text="Edad:")
        label_edad.pack()
        entry_edad=tk.Entry(ventana)
        entry_edad.pack()
        
        label_estatura=tk.Label(ventana,text="Estatura (cm):")
        label_estatura.pack()
        entry_estatura=tk.Entry(ventana)
        entry_estatura.pack()
        
        label_telefono=tk.Label(ventana,text="Teléfono:")
        label_telefono.pack()
        entry_telefono=tk.Entry(ventana)
        entry_telefono.pack()
        
        label_genero=tk.label(ventana,text"Género")
        label_genero.pack()
        
        rb_hombre=tk.Radiobutton(ventana,text="Hombre",variable=var_genero,value=1)
        rb_hombre.pack()
        
        rb_mujer=tk.Radiobutton(ventana,text="Mujer",variable=var_genero,value=2)
        rb=mujer.pack()
        
        #Boton para guardar datos 
        btn_guardar=tk.Button(ventana,text="Guardar"command=guardar_datos)
        btn_guardar.pack()
        #Boton para borrar campos
        btn=borrar=tk.Button(ventana,text="Borrar campos",command=limpiar_campos)
        btn_borrar.pack()
        
        #iniciar la aplicación
        ventana.mainloop()
