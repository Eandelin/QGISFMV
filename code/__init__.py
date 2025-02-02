# -*- coding: utf-8 -*-
import sys
try:
    sys.path.append(
        "D:\eclipse\plugins\org.python.pydev.core_7.1.0.201902031515\pysrc")
    from pydevd import *
except ImportError:
    None

from QGIS_FMV.utils.QgsFmvInstaller import WindowsInstaller
import platform
windows = platform.system() == 'Windows'
from QGIS_FMV.utils.QgsUtils import QgsUtils as qgsu
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.utils import iface
from qgis.utils import reloadPlugin
from qgis.core import Qgis as QGis
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QApplication

# Check dependencies
if windows:
    try:
        QApplication.setOverrideCursor(Qt.PointingHandCursor)
        QApplication.processEvents()
        WindowsInstaller()
        reloadPlugin('QGIS_FMV')
        iface.messageBar().pushMessage("QGIS FMV", "QGIS Full Motion Video installed correctly", QGis.Info, 3)
        QApplication.restoreOverrideCursor()
    except Exception as e:
        QApplication.restoreOverrideCursor()
        None
#         buttonReply = qgsu.CustomMessage("QGIS FMV", "", "you need to restart your QGIS,Do you really close?", icon="Information")
#         if buttonReply == QMessageBox.Yes:
#             # TODO : Restart QGIS
#             iface.actionExit().trigger()


def classFactory(iface):
    from .QgsFmv import Fmv
    return Fmv(iface)
