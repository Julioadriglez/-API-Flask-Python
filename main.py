from flask import Flask  """ se importa flask de los modulos de python """

app = Flask(__name__) # Se crea servidor y se guarda en app

@app.rout('/app/v1/users')   #  se define la dirección de la ruta 

def user_action():  # imprime una acción como respuesta de la petición 
    print("estoy aca")
    return "tu usuario"

app.run(debug = True)