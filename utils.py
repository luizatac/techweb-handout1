def extract_route(request):
    componentes = request.split()

    # Verifica se existem componentes suficientes e se o método HTTP está presente
    if len(componentes) >= 2 and componentes[1].startswith('/'):
        # Retorna a rota do componente 1, excluindo o primeiro caractere '/'
        return componentes[1][1:]
    else:
        return ''


from pathlib import Path

def read_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

import json
from pathlib import Path

def load_data(file_name):
    file_path = Path("data") / file_name

    try:
        # Abre o arquivo JSON no modo de leitura
        with open(file_path, 'r') as file:
            # Carrega o conteúdo do arquivo JSON como um objeto Python
            data = json.load(file)
            return data
    except FileNotFoundError:
        # Trate a exceção se o arquivo não for encontrado
        print(f"O arquivo não foi encontrado.")
        return None
    except json.JSONDecodeError as e:
        return None
    except Exception as e:

        print(f"Erro ao ler o arquivo ")
        return None

import os

def load_template(template_name):
    template_path = os.path.join("templates", template_name)
    return open(template_path, "r", encoding="utf-8").read()


def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        response = f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'
    else:
        response = f'HTTP/1.1 {code} {reason}\n\n{body}'
    return response.encode()

def save_data(lista):
    with open('data/notes.json', 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
        
def add_annotation_to_notes(nova_anotacao):
    notes_data = load_data('notes.json')

    notes_data.append(nova_anotacao)
    save_data(notes_data)