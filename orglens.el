;;; orglens.el --- Interactúa con OrgLens desde Emacs

;;; Commentary:
;; Este módulo permite ejecutar orglens-direct desde Emacs y ver los resultados en un buffer.
;; Soporta la entrada de múltiples archivos o patrones como texto libre.

;;; Code:

(defun orglens-run-direct (args)
  "Ejecuta orglens-direct con ARGS y muestra los resultados en un buffer."
  (let ((buffer-name "*OrgLens Results*")
        (command (concat "orglens-direct " args)))
    ;; Crear o reutilizar el buffer de resultados
    (with-current-buffer (get-buffer-create buffer-name)
      (erase-buffer)
      (insert (shell-command-to-string command))
      (display-buffer buffer-name))))

(defun orglens-search ()
  "Interfaz interactiva para buscar términos con orglens-direct."
  (interactive)
  (let* ((default-directory (expand-file-name default-directory)) ; Directorio actual
         (search-terms (read-string "Términos a buscar ('si') (opcional): "))
         (exclude-terms (read-string "Términos a excluir ('no') (opcional): "))
         (format (completing-read "Formato de salida: " '("txt" "json" "org" "md" "csv" "html")))
         (input-files (read-string "Archivos/patrones .org de entrada (ejemplo: *.org test/*.org): "))
         (output-files (read-string "Archivos de salida, acepta los formatos: org, txt, csv, json, md, html: "))
         (args ""))
    ;; Construir los argumentos dinámicamente
    (when (and search-terms (not (string-blank-p search-terms)))
      (setq args (concat args " -s " search-terms)))
    (when (and exclude-terms (not (string-blank-p exclude-terms)))
      (setq args (concat args " -n " exclude-terms)))
    (when format
      (setq args (concat args " -f " format)))
    (when (and input-files (not (string-blank-p input-files)))
      (setq args (concat args " -i " input-files)))
    (when (and output-files (not (string-blank-p output-files)))
      (setq args (concat args " -o " output-files)))
    ;; Ejecutar orglens-direct con los argumentos construidos
    (orglens-run-direct (substring args 1)))) ; Eliminar el primer espacio

(provide 'orglens)

;;; orglens.el ends here
