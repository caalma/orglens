#!/bin/bash

# Variables
BIN_DIR="$HOME/.local/bin"
BASHRC="$HOME/.bashrc"
COMPLETION_SCRIPT="orglens-completion.bash"

# Verificar si ~/.local/bin existe
if [ ! -d "$BIN_DIR" ]; then
    echo "Creando directorio $BIN_DIR..."
    mkdir -p "$BIN_DIR"
fi

# Dar permisos de ejecución
echo "Aplicando permisos de ejecición..."
chmod +x "./orglens-direct.py"
chmod +x "./orglens-interactive.py"

# Crear enlaces simbólicos
echo "Creando enlaces simbólicos en $BIN_DIR..."
ln -sf "$(pwd)/orglens-direct.py" "$BIN_DIR/orglens-direct"
ln -sf "$(pwd)/orglens-interactive.py" "$BIN_DIR/orglens-interactive"

# Agregar autocompletado a .bashrc
if  ! grep -q "$COMPLETION_SCRIPT" "$BASHRC" ; then
    echo "Configurando autocompletado en $BASHRC..."
    echo -e "\n# Autocompletado para OrgLens" >> "$BASHRC" >> "$BASHRC"
    echo "if [[ -f \"$(pwd)/$COMPLETION_SCRIPT\" ]]; then" >> "$BASHRC"
    echo "source \"$(pwd)/$COMPLETION_SCRIPT\"" >> "$BASHRC"
    echo "fi" >> "$BASHRC"
else
    echo "El autocompletado ya está configurado en $BASHRC."
fi

# Notificar al usuario
echo "Instalación completa."
echo "Por favor, recarga tu shell con 'source $BASHRC' o reinicia tu terminal."
