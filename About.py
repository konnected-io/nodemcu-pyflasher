
# coding=utf-8

import sys
import os
import wx
import wx.html
import wx.lib.wxpTag
import webbrowser
from Main import __version__

# ---------------------------------------------------------------------------


class AboutDlg(wx.Dialog):
    text = '''
<html>
<body bgcolor="#DCDCDC" style="font-family: Arial; background-color: #DCDCDC;">
<center>
    <img src="{0}/images/konnected-blue.png" width="292" height="55" alt="Konnected">

    <h1>Konnected Flash Tool</h1>
    <h3>based on NodeMCU PyFlasher</h3>
    <h4>by Marcel St&ouml;r</h4>

    <p>Version {1}</p>

    <p>Original NodeMCU PyFlasher <a style="color: #004CE5;" href="https://github.com/marcelstoer/nodemcu-pyflasher">project on
    GitHub</a>.</p>

    <p>This application was built from the <a style="color: #004CE5;" href="https://github.com/konnected-io/nodemcu-pyflasher">Konnected
    fork</a> on GitHub.</p>
    
    <p>For help and support, please visit <a style="color: #004CE5;" href="https://help.konnected.io">help.konnected.io</a>.

    <p>Original work &copy; 2018 Marcel St&ouml;r.<br/>
    Modifications &copy; 2018 Konnected, Inc<br/>
    Open source under the MIT license.</p>

    <p>
        <wxp module="wx" class="Button">
            <param name="label" value="Close">
            <param name="id" value="ID_OK">
        </wxp>
    </p>
</center>
</body>
</html>
'''

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "About Konnected Flash Tool")
        html = HtmlWindow(self, wx.ID_ANY, size=(420, -1))
        if "gtk2" in wx.PlatformInfo or "gtk3" in wx.PlatformInfo:
            html.SetStandardFonts()
        txt = self.text.format(self._get_bundle_dir(), __version__)
        html.SetPage(txt)
        ir = html.GetInternalRepresentation()
        html.SetSize((ir.GetWidth() + 25, ir.GetHeight() + 25))
        self.SetClientSize(html.GetSize())
        self.CentreOnParent(wx.BOTH)

    @staticmethod
    def _get_bundle_dir():
        # set by PyInstaller, see http://pyinstaller.readthedocs.io/en/v3.2/runtime-information.html
        if getattr(sys, 'frozen', False):
            return sys._MEIPASS
        else:
            return os.path.dirname(os.path.abspath(__file__))


class HtmlWindow(wx.html.HtmlWindow):
    def OnLinkClicked(self, link):
        webbrowser.open(link.GetHref())

# ---------------------------------------------------------------------------
