from flask import Flask,render_template

app=Flask(__name__,template_folder='../vista',static_folder='../static')

@app.route('/')
def inicio():
    return render_template('comunes/index.html')

@app.route('/pizzas')
def pedidos():
    return render_template('pizzas/pizzas_principal.html')

@app.route('/login')
def login():
    return render_template('usuarios/login.html')

@app.route('/registrar')
def registro():
    return render_template('usuarios/registro.html')

@app.route('/pedidos')
def pedidosclientes():
    return render_template('pedidos/pedidos_domicilio.html')

if __name__=='__main__':
    app.run(debug=True)
