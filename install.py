import os
import shutil
import sys
import subprocess

# Modelo do arquivo .desktop, incluindo o campo Path
desktop_entry = """
[Desktop Entry]
Version=1.0
Name=Dialise GUI
Comment=Interface gráfica para diálise peritoneal automatizada
Exec=python3 {exec_path}
Icon={icon_path}
Terminal=false
Type=Application
Categories=Utility;
Path={working_dir}
"""

# Função para verificar se os requisitos estão instalados
def instalar_requisitos():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print("Erro ao instalar dependências:", e)

# Função para criar o arquivo .desktop
def criar_arquivo_desktop(exec_path, icon_path, working_dir):
    user_desktop_dir = os.path.join(os.path.expanduser("~"), ".local/share/applications")
    if not os.path.exists(user_desktop_dir):
        os.makedirs(user_desktop_dir)
    
    desktop_file_path = os.path.join(user_desktop_dir, "dialise_gui.desktop")
    
    with open(desktop_file_path, 'w') as f:
        f.write(desktop_entry.format(exec_path=exec_path, icon_path=icon_path, working_dir=working_dir))
    
    os.chmod(desktop_file_path, 0o755)
    print(f"Arquivo .desktop criado em {desktop_file_path}")

# Função para copiar o ícone
def copiar_icone():
    icon_src = "images/icon.svg"
    icon_dest = os.path.join(os.path.expanduser("~"), ".local/share/icons", "dialise_icon.svg")
    
    if not os.path.exists(os.path.dirname(icon_dest)):
        os.makedirs(os.path.dirname(icon_dest))
    
    shutil.copy(icon_src, icon_dest)
    print(f"Ícone copiado para {icon_dest}")
    return icon_dest

# Função principal de instalação
def instalar():
    print("Instalando dependências...")
    instalar_requisitos()
    
    exec_path = os.path.abspath("dialise_gui.py")
    icon_path = copiar_icone()
    working_dir = os.path.dirname(exec_path)  # Define o diretório de trabalho como o diretório do script

    print("Criando arquivo .desktop...")
    criar_arquivo_desktop(exec_path, icon_path, working_dir)
    print("Instalação completa!")

if __name__ == "__main__":
    instalar()
