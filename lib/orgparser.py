import re
from lib.utils import *

class OrgParser:
    def __init__(self):
        self.tree = []

    def parse(self, file_path):
        """
        Analiza un archivo .org y construye una estructura de árbol jerárquica.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        current_level = None
        stack = []
        for line in lines:
            line = line.rstrip()
            match = re.match(r'(\*+)\s+(.*)', line)
            if match:
                level = len(match.group(1))
                title = match.group(2)
                node = {'level': level, 'title': title, 'content': []}

                while stack and stack[-1]['level'] >= level:
                    stack.pop()

                if stack:
                    stack[-1]['content'].append(node)
                else:
                    self.tree.append(node)

                stack.append(node)
            elif stack:
                stack[-1]['content'].append(line)

        return self.tree

    def search(self, query, negative_query=None, use_regex=False):
        """
        Busca una cadena específica en el árbol y devuelve las secciones que coinciden.
        """
        results = []
        match_function = re.search if use_regex else lambda q, t: q in t

        def recursive_search(node):
            normalized_title = normalize_text(node['title'])
            # Extraer solo el contenido textual para normalizar
            textual_content = ' '.join(
                item if isinstance(item, str) else ''
                for item in node['content']
            )
            normalized_content = normalize_text(textual_content)

            matches_positive = not query or any(
                match_function(q, normalized_title) or match_function(q, normalized_content)
                for q in query
            )
            matches_negative = any(
                match_function(nq, normalized_title) or match_function(nq, normalized_content)
                for nq in (negative_query or [])
            )

            if matches_positive and not matches_negative:
                results.append(node)

            for child in node['content']:
                if isinstance(child, dict):
                    recursive_search(child)

        for root in self.tree:
            recursive_search(root)

        return results
