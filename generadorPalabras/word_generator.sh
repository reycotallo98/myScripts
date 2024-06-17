#!/bin/bash

# Función para mostrar la ayuda
show_help() {
  echo "Uso: $0 <longitud>"
  echo
  echo "Genera una wordlist con todas las combinaciones posibles de los caracteres A-Z, a-z, y 0-9."
  echo
  echo "Opciones:"
  echo "  --help        Muestra esta ayuda y sale"
}

# Verificación de argumentos
if [ "$1" == "--help" ]; then
  show_help
  exit 0
elif [ -z "$1" ]; then
  echo "Error: Se requiere un argumento."
  echo "Use --help para más información."
  exit 1
fi

# Asignar la longitud de las palabras desde el primer argumento
length=$1

# Caracteres permitidos: A-Z, a-z, 0-9
chars=({A..Z} {a..z} {0..9})

# Función para generar las combinaciones
generate_combinations() {
  local current_length=$1
  local prefix=$2

  if [ "$current_length" -eq 0 ]; then
    echo "$prefix"
  else
    for char in "${chars[@]}"; do
      generate_combinations $((current_length - 1)) "$prefix$char"
    done
  fi
}

# Generar combinaciones y guardarlas en un archivo de wordlist
output_file="wordlist.txt"
> "$output_file"  # Limpiar el archivo antes de escribir

generate_combinations "$length" "" >> "$output_file"

echo "Wordlist generada en $output_file"
