from flask import Flask, render_template_string, request, redirect
import views
import utils

utils.iniciar_db()

app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())

@app.route('/delete/<int:NOTA_ID>')
def delete_route(NOTA_ID):
    views.deletar_nota(NOTA_ID)

    return redirect('/')

@app.route('/update/<int:NOTA_ID>')
def update_route(NOTA_ID):
    return render_template_string(views.update(NOTA_ID))

@app.route('/updatefact/<int:NOTA_ID>', methods=['POST'])
def update_route_fact(NOTA_ID):
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.editar_nota(NOTA_ID, titulo, detalhes)
    return redirect('/')

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)