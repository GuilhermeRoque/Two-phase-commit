# Two-phase-commit

Para executar o código:
1. Instalar o especificado em "requirements.txt"
2. Ir até o diretório raiz e executar python3 app.py

Obs: É utilizado um banco de dados sqlite para persistência dos dados, 
por isso para não haver conflito é necessário que coordenador e réplicas sejam máquinas diferentes.

Obs:O serviço um socket TCP com ip localhost e porta 5500.

