import markdown
from markdown.inlinepatterns import Pattern

# Only catch strings starting with http://, https:// or www
# but not preceeded by a " or a > (link is already done)
EXTRA_AUTOLINK_RE = r'(?<!"|>)((https?://|(?<!http://)(?<!https://)www)[-\w./#?%=&]+)'  # noqa


class AutoLinkPattern(Pattern):
    def handleMatch(self, m):
        el = markdown.util.etree.Element('a')
        if m.group(2).startswith('http'):
            href = m.group(2)
        else:
            href = 'http://%s' % m.group(2)
        el.set('href', href)
        el.text = m.group(2)
        return el


class AutoLinkExtension(markdown.Extension):
    """
    Make links without tag clickable.

    There's already an inline pattern called autolink which handles
    <http://www.google.com> type links. So lets call this extra_autolink.

    Based on: http://stackoverflow.com/a/1665440/119937
    """

    def extendMarkdown(self, md):
        md.inlinePatterns.register(
            AutoLinkPattern(EXTRA_AUTOLINK_RE),
            'extra_autolink',
            115
        )
