from flask import Flask    # Importa modulo Flask
from flask import request #importa modulo request

app = Flask(__name__) # Se crea servidor y se guarda en app

@app.route('/<id>', methods = ["GET", "POST"])   #  se define la dirección de la ruta 

def saludo(id):  # imprime una acción como respuesta de la petición 
    print(request.method)  # Imprime lo que pasa request y lo imprime en la consola 
    if( request.method == "POST"):
        print("Guardado en la base de datos")
        return " Guardado"
    else:
        print("recurso obtenido")
        return  "El id que me pides es el "+id

app.run(debug = True)