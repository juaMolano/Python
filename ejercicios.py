hora = input("ingresa la hora") 

if "am" in hora:
    periodo = "am"
    hora_num = hora.replace("am" , "")
elif "pm" in hora:
    periodo = "pm"
    hora_num = hora.replace("pm", "")
else:
    print("formato invalido")
    exit()

h, m = hora_num.split(":")
h = int(h)
m = int(m)

if periodo =="am":
   if h == 12:
       h = 0
elif periodo == "pm":
     if h !=12:
         h += 12

print (f"{h:02d}:{m:02d}")