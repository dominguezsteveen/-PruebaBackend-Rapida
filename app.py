from flask import Flask, jsonify, request

#
app = Flask(__name__)

#Rutas
@app.route('/')
def index():
    return jsonify({"message":"Successful!"})

@app.route('/palindromo', methods=['POST'])
def palindromo():
    def hallarPalindromo(cadena):
        if len(cadena)<=1:
            return cadena
        subcadena = ""
        for i in range(len(cadena)):
            for j in reversed(range(i,len(cadena))):
                if cadena[i] == cadena[j] and i!=j:
                    if len(cadena[i:j+1]) > len(subcadena):
                        candidata = cadena[i:j+1]
                        candidata = candidata[::-1]
                        if cadena[i:j+1] == candidata:
                            subcadena = candidata
                    
        if subcadena != "": 
            return subcadena 
        else: return "<No se encontró palindromo>"
    
    try:
        if request.json:
            if 'user' in request.json:
                user = str(request.json['user'])
            else:
                return jsonify({"message":"Error!, hace falta la clave 'user' en el objeto JSON"})
            if 'password' in request.json:
                password = str(request.json['password'])
            else:
                return jsonify({"message":"Error!, hace falta la clave 'password' en el objeto JSON"})
            if 'cadena' in request.json:
                cadena = str(request.json['cadena'])
            else:
                return jsonify({"message":"Error!, hace falta la clave 'cadena' en el objeto JSON"})
        else:
            return jsonify({"message":"Error!, se espera un objeto JSON con la claves 'cadena','user' and 'password'"})
        
        if user == "admin" and password == "4DM!N":
            resultado = "La subcadena más larga de '"+cadena+"' es '"+hallarPalindromo(cadena)+"'"
            return jsonify({"message":"Successful!", "result":resultado})
        else:
            return jsonify({"message":"Error!, Usuario o contraseña no validos"})
        
        
    except ValueError as error:
        return jsonify({"message":"Error!,"+error})

if __name__ == '__main__':
    app.run(debug=True, port=4000)