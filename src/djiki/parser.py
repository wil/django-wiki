import re
from creole import Parser
from creole.html_emitter import HtmlEmitter
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from . import models, utils

class DjikiHtmlEmitter(HtmlEmitter):
	image_params_re = re.compile(r'^(?:(?P<size>[0-9]+x[0-9]+)(?:\||$))?(?P<title>.*)$')

	def header_emit(self, node):
		return u'<a name="%s"></a><h%d>%s</h%d>\n' % (
			utils.anchorize(node.content),
			node.level + 1,
			self.html_escape(node.content),
			node.level)

	def link_emit(self, node):
		target = node.content
		if node.children:
			inside = self.emit_children(node)
		else:
			inside = self.html_escape(target)
		m = self.link_rules.addr_re.match(target)
		if m:
			if m.group('extern_addr'):
				return u'<a href="%s">%s</a>' % (
					self.attr_escape(target), inside)
			elif m.group('inter_wiki'):
				raise NotImplementedError
		return u'<a href="%s">%s</a>' % (
			reverse('djiki-page-view', kwargs={'title': utils.urlize_title(self.attr_escape(target))}),
			inside)

def render(src):
	doc = Parser(src).parse()
	return DjikiHtmlEmitter(doc).emit().encode('utf-8', 'ignore')