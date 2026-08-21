from utils import obter_notas, load_template, adicionar_nota, deletar_nota

def index():
    note_template = load_template('components/note.html')
    notas = obter_notas()

    notes_list = [note_template.format(title=dados[1], details=dados[2], id=dados[0]) for dados in notas]

    notes = '\n'.join(notes_list)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    adicionar_nota(titulo, detalhes)

def delet(nota_id):
    deletar_nota(nota_id)