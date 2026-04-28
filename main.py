# organizador de arquivos
from pathlib import Path
import shutil
from tkinter.filedialog import askdirectory




pasta_origem = Path(askdirectory(title="Selecione a pasta para organizar"))

for arquivo in pasta_origem.iterdir():
    if arquivo.is_file():
        extensao = arquivo.suffix
        pasta_destino = pasta_origem / extensao
        pasta_destino.mkdir(exist_ok=True)
        shutil.move(arquivo, pasta_destino)
print("Organização concluída!")
