_orglens_direct_completion() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # Opciones principales
    opts="-s -n -f -o -i -r --help"

    # Completar opciones
    case "${prev}" in
        -s|-n)
            # No completar nada después de -s o -n (términos de búsqueda/libres)
            return
            ;;
        -f)
            # Formatos soportados
            COMPREPLY=( $(compgen -W "json txt org md csv html" -- "${cur}") )
            return
            ;;
        -o|-i)
            # Completar archivos/directorios
            COMPREPLY=( $(compgen -f -- "${cur}") )
            return
            ;;
    esac

    # Completar opciones principales si no hay coincidencia previa
    if [[ "${cur}" == -* ]]; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
        return
    fi

    # Completar archivos .org por defecto
    COMPREPLY=( $(compgen -f -X '!*.org' -- "${cur}") )
}

complete -F _orglens_direct_completion orglens-direct
