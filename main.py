from flask import Flask  

app = Flask(__name__) # Se crea servidor y se guarda en app

@app.route('/app/v1/users')   #  se define la dirección de la ruta 

def user_action():  # imprime una acción como respuesta de la petición 
    print("estoy aca")
    return "tu usuario"

app.run(debug = True)