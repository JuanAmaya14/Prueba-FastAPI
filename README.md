# Crear .venv
### 1. Instalar el entorno usa:
```bash
python -m venv .venv 
```
### 2. Activa el entorno:
```bash
.venv\Scripts\Activate.ps1
```
### 3. Actualiza pip:
```bash
python -m pip install --upgrade pip
```
### 4. Instala FastAPi en el entorno:
```bash
pip install "fastapi[standard]"
```
### 5. Arranca FastAPI
```bash
fastapi dev src/main.py
```
### 6. Para desactivar .venv
```bash
deactivate
```