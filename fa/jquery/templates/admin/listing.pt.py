registry = dict(version=0)
def bind():
    from cPickle import loads as _loads
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
    _attrs_4362992784 = _loads('(dp1\n.')
    _attrs_4362992848 = _loads('(dp1\nVclass\np2\nVfa_controls\np3\ns.')
    _attrs_4362992528 = _loads('(dp1\n.')
    _attrs_4362992656 = _loads('(dp1\n.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    def render(econtext, rcontext=None):
        macros = econtext.get('macros')
        _translate = econtext.get('_translate')
        _slots = econtext.get('_slots')
        target_language = econtext.get('target_language')
        u'_init_stream()'
        (_out, _write, ) = _init_stream()
        u'_init_tal()'
        (_attributes, repeat, ) = _init_tal()
        u'_init_default()'
        _default = _init_default()
        u'None'
        default = None
        u'None'
        _domain = None
        u"main.macros['master']"
        _metal = _lookup_attr(econtext['main'], 'macros')['master']
        def _callback_javascript(econtext, _repeat, _out=_out, _write=_write, _domain=_domain, **_ignored):
            if _repeat:
                repeat.update(_repeat)
            attrs = _attrs_4362992528
            u"request.registry.settings.get('fa.use_popup') and 'true' or 'false'"
            _write(u'<script>\n      var USE_POPUP = ')
            _tmp1 = ((_lookup_attr(_lookup_attr(_lookup_attr(econtext['request'], 'registry'), 'settings'), 'get')('fa.use_popup') and 'true') or 'false')
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, unicode, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, unicode):
                    _tmp = str(_tmp)
                if ('&' in _tmp):
                    if (';' in _tmp):
                        _tmp = _re_amp.sub('&amp;', _tmp)
                    else:
                        _tmp = _tmp.replace('&', '&amp;')
                if ('<' in _tmp):
                    _tmp = _tmp.replace('<', '&lt;')
                if ('>' in _tmp):
                    _tmp = _tmp.replace('>', '&gt;')
                _write(_tmp)
            u"request.static_url('fa.jquery:jquery-ui/jqgrid/js/i18n/grid.locale-en.js')"
            _write(u';\n      jQuery.fa.add_resource("')
            _tmp1 = _lookup_attr(econtext['request'], 'static_url')('fa.jquery:jquery-ui/jqgrid/js/i18n/grid.locale-en.js')
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, unicode, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, unicode):
                    _tmp = str(_tmp)
                if ('&' in _tmp):
                    if (';' in _tmp):
                        _tmp = _re_amp.sub('&amp;', _tmp)
                    else:
                        _tmp = _tmp.replace('&', '&amp;')
                if ('<' in _tmp):
                    _tmp = _tmp.replace('<', '&lt;')
                if ('>' in _tmp):
                    _tmp = _tmp.replace('>', '&gt;')
                _write(_tmp)
            u"request.static_url('fa.jquery:jquery-ui/jqgrid/js/jquery.jqGrid.min.js')"
            _write(u'");\n      jQuery.fa.add_resource("')
            _tmp1 = _lookup_attr(econtext['request'], 'static_url')('fa.jquery:jquery-ui/jqgrid/js/jquery.jqGrid.min.js')
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, unicode, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, unicode):
                    _tmp = str(_tmp)
                if ('&' in _tmp):
                    if (';' in _tmp):
                        _tmp = _re_amp.sub('&amp;', _tmp)
                    else:
                        _tmp = _tmp.replace('&', '&amp;')
                if ('<' in _tmp):
                    _tmp = _tmp.replace('<', '&lt;')
                if ('>' in _tmp):
                    _tmp = _tmp.replace('>', '&gt;')
                _write(_tmp)
            u"request.static_url('fa.jquery:jquery-ui/jqgrid/js/fa.jqgrid.js')"
            _write(u'");\n      jQuery.fa.add_resource("')
            _tmp1 = _lookup_attr(econtext['request'], 'static_url')('fa.jquery:jquery-ui/jqgrid/js/fa.jqgrid.js')
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, unicode, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, unicode):
                    _tmp = str(_tmp)
                if ('&' in _tmp):
                    if (';' in _tmp):
                        _tmp = _re_amp.sub('&amp;', _tmp)
                    else:
                        _tmp = _tmp.replace('&', '&amp;')
                if ('<' in _tmp):
                    _tmp = _tmp.replace('<', '&lt;')
                if ('>' in _tmp):
                    _tmp = _tmp.replace('>', '&gt;')
                _write(_tmp)
            u"request.static_url('fa.jquery:jquery-ui/jqgrid/css/ui.jqgrid.css')"
            _write(u'");\n      jQuery.fa.add_resource("')
            _tmp1 = _lookup_attr(econtext['request'], 'static_url')('fa.jquery:jquery-ui/jqgrid/css/ui.jqgrid.css')
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, unicode, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, unicode):
                    _tmp = str(_tmp)
                if ('&' in _tmp):
                    if (';' in _tmp):
                        _tmp = _re_amp.sub('&amp;', _tmp)
                    else:
                        _tmp = _tmp.replace('&', '&amp;')
                if ('<' in _tmp):
                    _tmp = _tmp.replace('<', '&lt;')
                if ('>' in _tmp):
                    _tmp = _tmp.replace('>', '&gt;')
                _write(_tmp)
            _write(u'");\n    </script>\n')
        def _callback_main(econtext, _repeat, _out=_out, _write=_write, _domain=_domain, **_ignored):
            if _repeat:
                repeat.update(_repeat)
            attrs = _attrs_4362992656
            u"''"
            _write(u'<div>\n      ')
            _default.value = default = ''
            u"fs.render(renderer='fa.jquery:templates/forms/jqgrid.pt', request=request)"
            _content = _lookup_attr(econtext['fs'], 'render')(renderer='fa.jquery:templates/forms/jqgrid.pt', request=econtext['request'])
            attrs = _attrs_4362992784
            u'_content'
            _write(u'<div>')
            _tmp1 = _content
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, unicode, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, unicode):
                    _tmp = str(_tmp)
                _write(_tmp)
            u"u'\\n      '"
            _write(u'</div>\n      ')
            _default.value = default = u'\n      '
            u'actions.buttons(request)'
            _content = _lookup_attr(econtext['actions'], 'buttons')(econtext['request'])
            attrs = _attrs_4362992848
            u'_content'
            _write(u'<div class="fa_controls">')
            _tmp1 = _content
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, unicode, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, unicode):
                    _tmp = str(_tmp)
                _write(_tmp)
            _write(u'</div>\n    </div>\n')
        u"{'main': _callback_main, 'javascript': _callback_javascript}"
        _tmp = {'main': _callback_main, 'javascript': _callback_javascript, }
        u"main.macros['master']"
        _metal.render(_tmp, _out=_out, _write=_write, _domain=_domain, econtext=econtext)
        return _out.getvalue()
    return render

__filename__ = '/Users/gawel/py/formalchemy_project/fa.jquery/fa/jquery/templates/admin/listing.pt'
registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
