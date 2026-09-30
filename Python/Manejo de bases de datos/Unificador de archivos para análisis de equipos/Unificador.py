import pandas as pd
from tkinter import Tk, filedialog, messagebox
from datetime import datetime
from functools import reduce
from tkinter import filedialog




def seleccionar_archivo_DUT():
    elegir = True
    df_total = pd.DataFrame()
    root = Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)  
    root.update() 
    
    
    
    while elegir:
       


        
        ruta = filedialog.askopenfilename(title="Selecciona el archivo DUT")
        if not ruta:
            messagebox.showinfo("Sin archivo","No se seleccionó ningún archivo.")
            
            return None
        
        if "DUT" not in ruta:
            messagebox.showinfo("Sin archivo","No se seleccionó el archivo DUT.")
        
            return None
        
        try:
            with open(ruta,"r", encoding="utf-8") as f:
                lineas = f.readlines()
                fecha = None
                for linea in lineas[:7]:
                    if "Test Start Time" in linea:
                        fecha = datetime.strptime(linea.strip().split(",")[1],"%H:%M:%S %p")
                
            df = pd.read_csv(ruta, sep=",", skiprows=19)
            df = df.rename(columns={"Elapsed Time [s]": "Time"})
            df= df.rename(columns={"Mass [mg/m3]":"DUT Mass [mg/m3]"})
            df["Time"]= fecha + pd.to_timedelta(df["Time"],unit="s")
            
            df["Time"]= df["Time"].dt.strftime("%H:%M:%S")
           
            
            df_total = pd.concat([df_total,df],ignore_index= True)
         
            elegir = messagebox.askyesno("Otro archivo", "¿Desea seleccionar otro archivo DUT?")
           
           
            
                
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo leer el archivo:\n{e}")
            break
        
        
        
    messagebox.showinfo("Finalizando", "No se seleccionarán más archivos DUT")
    root.destroy()
    df_total = df_total[["Time","DUT Mass [mg/m3]"]]
   
    return df_total
DUT = seleccionar_archivo_DUT()


def seleccionar_archivo_CPC():
    elegir = True
    df_total = pd.DataFrame()
    root = Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)  
    root.update() 
    
    while elegir:
        
        ruta = filedialog.askopenfilename(title="Selecciona el archivo CPC")
        
        if not ruta:
            messagebox.showinfo("Sin archivo","No se seleccionó ningún archivo.")
            return None
        
        if "CPC" not in ruta:
            messagebox.showinfo("Sin archivo","No se seleccionó el archivo CPC.")
            return None
        
        try:
            
            df = pd.read_csv(ruta, sep=",", skiprows=17, encoding="latin1")
            df.rename(columns={"Concentration (#/cm³)":"CPC Concentration (#/cm3)"},inplace= True)
            
            
            df['Time'] = pd.to_datetime(df['Time'], format="mixed", dayfirst=True, errors='coerce')
            df = df[df["Time"].dt.second %10 ==0]
            
            df['Time'] = df['Time'].dt.strftime('%H:%M:%S')
          
            
            
            df_total = pd.concat([df_total,df],ignore_index= True)
         
            elegir = messagebox.askyesno("Otro archivo", "¿Desea seleccionar otro archivo CPC?")
           
           
            
                
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo leer el archivo:\n{e}")
            break
        
        
        
    messagebox.showinfo("Finalizando", "No se seleccionarán más archivos CPC")
    root.destroy()
    df_total=df_total[["Time","CPC Concentration (#/cm3)"]]
   
    return df_total
CPC = seleccionar_archivo_CPC()








def seleccionar_archivo_AE51():
    elegir = True
    df_total = pd.DataFrame()
    root = Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)  
    root.update() 
    
    while elegir:
        
        ruta = filedialog.askopenfilename(title="Selecciona el archivo AE51")
        
        if not ruta:
            messagebox.showinfo("Sin archivo","No se seleccionó ningún archivo.")
            return None
        
        if "AE51" not in ruta:
            messagebox.showinfo("Sin archivo","No se seleccionó el archivo AE51.")
            return None
        
        try:
            
            df = pd.read_csv(ruta,sep=",", skiprows=15,encoding="latin1")
            
            

            df.rename(columns={"ATN":"AE51 ATN",
                               "BC":"AE51 BC [ng/m3]",
                               "Time": "Time" },inplace=True)
           
            
            
            df_total = pd.concat([df_total,df],ignore_index= True)
         
            elegir = messagebox.askyesno("Otro archivo", "¿Desea seleccionar otro archivo AE51?")
           
           
            
                
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo leer el archivo:\n{e}")
            break
        
        
        
    messagebox.showinfo("Finalizando", "No se seleccionarán más archivos AE51")
    root.destroy()
    df_total = df_total[["Time","AE51 ATN","AE51 BC [ng/m3]"]]
   
    return df_total
AE51 = seleccionar_archivo_AE51()





def seleccionar_archivo_GPS():
    elegir = True
    df_total = pd.DataFrame()
    root = Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)  
    root.update() 
    
    while elegir:
        
        ruta = filedialog.askopenfilename(title="Selecciona el archivo GPS")
        
        if not ruta:
            messagebox.showinfo("Sin archivo","No se seleccionó ningún archivo.")
            return None
        
        if "GPS" not in ruta:
            messagebox.showinfo("Sin archivo","No se seleccionó el archivo GPS.")
            return None
        
        try:
            with open(ruta, 'r', encoding="latin-1") as f:
                lineas = f.readlines()
            
            for i, linea in enumerate(lineas):
                if linea.startswith("Header\tPosition"):
                    pos = i+2
                    break
            datos =[l.strip().split("\t")[1:4] for l in lineas[pos:] ]
            
             
            columnas = ["Position", "Time", "Altitude"]
            df = pd.DataFrame(datos,columns = columnas)   
            
      
        
            
            df['Time'] = pd.to_datetime(df['Time'], format="mixed", dayfirst=True, errors='coerce')
          
            df['Time'] = df['Time'].dt.strftime('%H:%M:%S')

           
                        
                        
            df_total = pd.concat([df_total,df],ignore_index= True)
         
            elegir = messagebox.askyesno("Otro archivo", "¿Desea seleccionar otro archivo GPS?")
           
           
            
                
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo leer el archivo:\n{e}")
            break
        
        
        
    messagebox.showinfo("Finalizando", "No se seleccionarán más archivos GPS")
    root.destroy()
   
    return df_total
GPS = seleccionar_archivo_GPS()


def unificador(DUT,CPC,AE51,GPS):
    dfs = [DUT,CPC,AE51,GPS]
    df_total = reduce(lambda left, right: pd.merge(left, right, on="Time", how ="outer"),dfs)
    
    nombre_archivo = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")],
        title="Guardar archivo unificado como"
    )

    if not nombre_archivo:
        print("No se seleccionó una ruta para guardar el archivo.")
        return df_total

    try:
        df_total.to_excel(nombre_archivo, index=False)
        print(f"Archivo Excel generado correctamente: {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el archivo Excel: {e}")
    
    return df_total
    
    
df_total= unificador(DUT,CPC,AE51,GPS)
    