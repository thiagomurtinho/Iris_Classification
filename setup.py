import os
import sys
import subprocess

if sys.platform.startswith('win'):
  subprocess.run(["pip", "install", "-r", "requirements.txt"])
  subprocess.run(["python","main.py"])
else:
  try:
    subprocess.run(["python3","-m","pip", "install", "-r", "requirements.txt"])
    subprocess.run(["pythone","main.py"])
  except:
    print("[ERROR]: Erro ao instalar os requirements. Instale os requirements manualmente pelo requirements.txt. Use algo parecido com 'pip install -r requirements.txt'")
