'''
c2corg p Extension for Python-Markdown
==============================================

Converts tags [p] to div with clear:both
'''

from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from markdown.util import etree
import re

P_RE = r'(?:\n|^)\[p\](?:\n|$)'


class C2CPTagExtension(Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(
            C2CPTag(md.parser),
            'c2cptag',
            13
        )


class C2CPTag(BlockProcessor):
    RE = re.compile(P_RE)

    def test(self, parent, block):
        return bool(self.RE.search(block))

    def run(self, parent, blocks):
        block = blocks.pop(0)
        m = self.RE.search(block)

        before = block[:m.start()]
        self.parser.parseBlocks(parent, [before])

        parent.append(etree.Element('div', {"style": "clear:both"}))

        after = block[m.end():]
        self.parser.parseBlocks(parent, [after])
