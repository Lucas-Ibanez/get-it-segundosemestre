from utils import obter_notas, load_template, adicionar_nota, deletar_nota, pegar_nota, edit

def index():
    note_template = load_template('components/note.html')
    notas = obter_notas()

    notes_list = [note_template.format(title=dados[1], details=dados[2], id=dados[0], id_edit=dados[0]) for dados in notas]

    notes = '\n'.join(notes_list)

    return load_template('index.html').format(notes=notes)

def update(nota_id):
    nota = pegar_nota(nota_id)
    return load_template('edit.html').format(titulo_nota=nota[0], conteudo_nota=nota[1], identify=nota[2], idd=nota[2])

def editar_nota(nota_id, title, details):
    edit(nota_id, title, details)

def submit(titulo, detalhes):
    adicionar_nota(titulo, detalhes)

def delet(nota_id):
    deletar_nota(nota_id)