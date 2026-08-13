import json

def load_data(nome_json):
    with open(f"static/data/{nome_json}", "r") as arquivo_json:
        conteudo_arquivo = arquivo_json.read()

    return json.loads(conteudo_arquivo)

def load_template(nome_template):
    with open(f"static/templates/{nome_template}", "r") as arquivo_template:
        conteudo_arquivo = arquivo_template.read()

    return conteudo_arquivo
