from utils import load_data, load_template
from urllib.parse import unquote_plus, parse_qs
from utils import add_annotation_to_notes

from utils import build_response

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]

        params = parse_qs(corpo)

        titulo = params.get('titulo', [''])[0]
        detalhes = params.get('detalhes', [''])[0]
        nova_anotacao = {'titulo': titulo, 'detalhes': detalhes}
        print(nova_anotacao)
        print("--------------------------")
        add_annotation_to_notes(nova_anotacao)

        # Return a redirect response for POST requests
        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    # Use build_response for the main response
    return build_response(body=load_template('index.html').format(notes=notes))