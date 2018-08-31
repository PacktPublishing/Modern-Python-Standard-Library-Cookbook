"""Extracts code snippets from rst files of each chapter"""
import sys
import os
from docutils.core import publish_doctree

with open(sys.argv[1]) as f:
    doctree = publish_doctree(f.read())

    count = 0
    titles = doctree.traverse(condition=lambda node: node.tagname == 'title')
    for idx, title in enumerate(titles):
        if title.astext() != 'How to do it':
            continue

        count += 1
        section = title.parent        
        code_blocks = section.traverse(condition=lambda node: node.tagname == 'literal_block')
        source_code = '\n'.join([block.astext() for block in code_blocks])

        chapter_name = os.path.basename(sys.argv[1]).split('.')[0]
        source_file = '%s/%s_%02d.py' % (chapter_name, chapter_name, count)
        if os.path.exists(source_file):
            continue

        try:
            os.makedirs(chapter_name)
        except:
            pass
        
        with open(source_file, 'w') as s:
            s.write(source_code)