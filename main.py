import webbrowser
from pathlib import Path
from jinja2 import Template

# 1. Lê o index.html e renderiza os dados
conteudo = Template(Path("index.html").read_text(encoding="utf-8")).render(nome="Carlos", idade=28)

# 2. Escreve direto em um arquivo temporário
arquivo_temp = Path("temp.html")
arquivo_temp.write_text(conteudo, encoding="utf-8")

# 3. Abre no navegador
webbrowser.open(arquivo_temp.absolute().as_uri())