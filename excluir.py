#comando que excluir as pastas
import shutil
#nome da pasta, poderia ser uma lista com varias pastas
dirPath = 'temp'

try:
    shutil.rmtree(dirPath)
except OSError as e:
    print(e.strerror)
