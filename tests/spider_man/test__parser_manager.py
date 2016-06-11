# -*- coding: utf-8 -*-
import unittest2
from spider_man.parser_manager import ParserManager


class TestParserManager(unittest2.TestCase):
    def test__parse(self):
        pm = ParserManager(r"/view/*", ".main-content dl dd h1")
        urls, data = pm.parse("""
         <!DOCTYPE html>
<!--STATUS OK-->
<html>
<body class="wiki-lemma normal">
<div class="body-wrapper">
<div class="content-wrapper">
<div class="content">
<div class="main-content">
<dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
<dd class="lemmaWgt-lemmaTitle-title">
<h1 >动态语言</h1>
<a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="lock-lemma" target="_blank" href="/view/10812319.htm" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
</dd>
</dl><div class="edit-prompt">本词条缺少<strong>名片图</strong>，补充相关内容使词条更完整，还能快速升级，赶紧来<a  class="edit-prompt-link j-edit-link">编辑</a>吧！</div>
<div class="lemma-summary" label-module="lemmaSummary">
<div class="anchor-list">
</div><div class="para-title level-2">
<h2 class="title-text"><span class="title-prefix">动态语言</span>动态语言</h2>
<a class="edit-icon j-edit-link" data-edit-dl="1" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para"><b>有三个名词容易混淆：</b></div>
<div class="para" label-module="para">Dynamic Programming Language (动态语言或动态编程语言)</div>
<div class="para" label-module="para">Dynamically Typed Language (动态类型语言)</div>
<div class="para" label-module="para">Statically Typed Language (静态类型语言)</div>
<div class="para-title level-2">
<h2 class="title-text"><span class="title-prefix">动态语言</span>未来发展</h2>
<a class="edit-icon j-edit-link" data-edit-dl="3" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
</div>
</div>
</div>
</div>
</body>
</html>
""")
        self.assertEqual(len(urls), 1)
        self.assertEqual(data[0].string, u"动态语言")