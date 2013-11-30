# -*- coding: utf-8 -*-

"""
/***************************************************************************
 BaseMapFrame
                                 A QGIS plugin

 Creates Japan national basemap frames.

                             -------------------
        begin                : 2013-05-03
        copyright            : (C) 2013 by Yamate, N
        email                : arctic_tern@mf-atelier.sakura.ne.jp
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

import resource
import math
from ui_selectSystem import Ui_DialogSelectSystem

from math import ceil,floor

class dlgSelectSystem(QDialog, Ui_DialogSelectSystem):
    
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.comboBox_system.addItem("I", (2443))
        self.comboBox_system.addItem("II", (2444))
        self.comboBox_system.addItem("III", (2445))
        self.comboBox_system.addItem("IV", (2446))
        self.comboBox_system.addItem("V", (2447))
        self.comboBox_system.addItem("VI", (2448))
        self.comboBox_system.addItem("VII", (2449))
        self.comboBox_system.addItem("VIII", (2450))
        self.comboBox_system.addItem("IX", (2451))
        self.comboBox_system.addItem("X", (2452))
        self.comboBox_system.addItem("XI", (2453))
        self.comboBox_system.addItem("XII", (2454))
        self.comboBox_system.addItem("XIII", (2455))
        self.comboBox_system.addItem("XIV", (2456))
        self.comboBox_system.addItem("XV", (2457))
        self.comboBox_system.addItem("XVI", (2458))
        self.comboBox_system.addItem("XVII", (2459))
        self.comboBox_system.addItem("XVIII", (2460))
        self.comboBox_system.addItem("XIX", (2461))
        self.comboBox_system.setCurrentIndex(8)
        self.radioButton_2500.setChecked(True)
        
        
    def onCheck2500(self):
        self.comboBox_system.setEnabled(True)
    
    
    def onCheck5000(self):
        self.comboBox_system.setEnabled(True)
    
    
    def onCheck2nd(self):
        self.comboBox_system.setEnabled(False)


def GetFrameName2500(x, y):
    y += 1500
    aFrame = ['A', 'A', '0', '0', '4']
    ny = (300000 - y) / 30000
    nx = (x + 160000) / 40000
    aFrame[0] = chr(ord(aFrame[0]) + ny)
    aFrame[1] = chr(ord(aFrame[1]) + nx)
    by = 300000 - ny * 30000
    bx = nx * 40000 - 160000
    ny = (by - y) / 3000
    nx = (x - bx) / 4000
    aFrame[2] = chr(ord(aFrame[2]) + ny)
    aFrame[3] = chr(ord(aFrame[3]) + nx)
    by -= ny * 3000
    bx += nx * 4000
    mx = x - bx
    my = by - y
    if mx == 0 and my == 0:
        aFrame[4] = '1'
    elif mx == 0:
        aFrame[4] = '3'
    elif my == 0:
        aFrame[4] = '2'
    strFrame = ""
    for c in aFrame:
        strFrame += c
    return strFrame


def GetFrameName5000(x, y):
    y += 3000
    aFrame = ['A', 'A', '0', '0']
    ny = (300000 - y) / 30000
    nx = (x + 160000) / 40000
    aFrame[0] = chr(ord(aFrame[0]) + ny)
    aFrame[1] = chr(ord(aFrame[1]) + nx)
    by = 300000 - ny * 30000
    bx = nx * 40000 - 160000
    ny = (by - y) / 3000
    nx = (x - bx) / 4000
    aFrame[2] = chr(ord(aFrame[2]) + ny)
    aFrame[3] = chr(ord(aFrame[3]) + nx)
    strFrame = ""
    for c in aFrame:
        strFrame += c
    return strFrame

def GetFrameName1stMesh(x, y):
    nName = (int(floor(y * 1.5)) * 100) + int(floor(x-100))
    return str(nName)

def GetFrameName2ndMesh(x, y):
    yMod = y*60 % 40
    xMod = (x % 1) * 60
    ny = int(yMod/5.0)
    nx = int(xMod/7.5)
    
    return GetFrameName1stMesh(x, y) + str(ny) + str(nx)

def generateFrames(layer, mapRect, width, height, mapCrs, elemCrs, xmin, xmax, ymin, ymax, nameFunc):

    trans = QgsCoordinateTransform(mapCrs, elemCrs)
    rect = trans.transform(mapRect)

    if rect.xMinimum() < xmin:
        rect.setXMinimum(xmin)
    if rect.xMaximum() > xmax:
        rect.setXMaximum(xmax)
    if rect.yMinimum() < ymin:
        rect.setYMinimum(ymin)
    if rect.yMaximum() > ymax:
        rect.setYMaximum(ymax)

    layer.startEditing()
    fields = layer.pendingFields()
    fields.append(QgsField("MapName", QVariant.String))
    layer.addAttribute(fields[0])
    y = (int(floor(rect.yMinimum() / height))) * height
    while y < rect.yMaximum():
        x = (int(floor(rect.xMinimum() / width))) * width
        while x < rect.xMaximum():
            pnt = trans.transform(QgsPoint(x, y), QgsCoordinateTransform.ReverseTransform)
            f = QgsFeature()
            f.setFields(fields,True)
            f.setGeometry(QgsGeometry.fromPolygon([[
                trans.transform(QgsPoint(x, y), QgsCoordinateTransform.ReverseTransform),
                trans.transform(QgsPoint(x, y + height), QgsCoordinateTransform.ReverseTransform),
                trans.transform(QgsPoint(x + width, y + height), QgsCoordinateTransform.ReverseTransform),
                trans.transform(QgsPoint(x + width, y), QgsCoordinateTransform.ReverseTransform),
                trans.transform(QgsPoint(x, y), QgsCoordinateTransform.ReverseTransform)
            ]]))
            
            strFrame = nameFunc(x, y)	
            
            f.setAttribute("MapName", strFrame)
            layer.addFeature(f)
            
            x += width
        y += height
                        
    layer.commitChanges()
    layer.updateExtents()

    
class BaseMapFrame(object):

    def __init__(self, iface):
        try:
            self.QgisVersion = unicode(QGis.QGIS_VERSION_INT)
        except:
            self.QgisVersion = unicode(QGis.qgisVersion)[0]

        self.iface = iface
        self.canvas = iface.mapCanvas()

    def initGui(self):
        self.action_genMesh = QAction(QIcon(":/icon/icon.png"), "BaseMapFrame", self.iface.mainWindow())
        self.iface.addVectorToolBarIcon(self.action_genMesh)
        self.iface.addPluginToVectorMenu(
            QCoreApplication.translate(
            "BaseMapFrame", "Creates Japan National Base Map Frame ..."), self.action_genMesh)

        QObject.connect(self.action_genMesh, SIGNAL("activated()"), self.genMesh)

    def unload(self):
        self.iface.removeVectorToolBarIcon(self.action_genMesh)
        self.iface.removePluginVectorMenu(QCoreApplication.translate(
            "BaseMapFrame", "Creates Japan National Base Map Frame ..."), self.action_genMesh)


    def checkExtent(self, rect, elemCrs, mapCrs):

        if rect.isEmpty():
            QMessageBox.information(self.iface.mainWindow(), "Warning",
                        QCoreApplication.translate("BaseMapFrame", "Map extent is empty.") )
            return False
        
        trans = QgsCoordinateTransform(mapCrs, elemCrs)
        
        try:
            rect_trans = trans.transform(rect)
        except QgsCsException:
            QMessageBox.information(self.iface.mainWindow(), "Warning", 
                QCoreApplication.translate("BaseMapFrame", "Map canvas extent out of range."))
            return False

        if rect_trans.xMaximum() < -160000 or rect_trans.xMinimum() > 160000 or rect_trans.yMaximum() < -300000 or rect_trans.yMinimum() > 300000:
            QMessageBox.information(self.iface.mainWindow(), "Warning", 
                QCoreApplication.translate("BaseMapFrame", "Map canvas extent out of range."))
            return False
            
        return True
    

    def genMesh(self):
        
        dlg = dlgSelectSystem()
        if dlg.exec_() == QDialog.Accepted:
            
            if not dlg.radioButton_2nd.isChecked():
                systemNo = dlg.comboBox_system.itemData(dlg.comboBox_system.currentIndex())
            else:
                systemNo = 4612

            mapRenderer = self.canvas.mapRenderer()
            mapCrs = mapRenderer.destinationCrs()
            elemCrs = QgsCoordinateReferenceSystem()
            elemCrs.createFromId(systemNo)
            mapRect = self.canvas.extent()
            
            if self.checkExtent(mapRect, elemCrs, mapCrs) == False:
                return
        
            if dlg.radioButton_2500.isChecked():
                latlonLayer = QgsVectorLayer("Polygon", "Base Map Frame 2500", "memory")
                QgsMapLayerRegistry.instance().addMapLayer(latlonLayer)
                generateFrames(latlonLayer, mapRect, 2000, 1500, mapCrs, elemCrs, -160000, 160000, -300000, 300000, GetFrameName2500);

            elif dlg.radioButton_5000.isChecked():
                latlonLayer = QgsVectorLayer("Polygon", "Base Map Frame 5000", "memory")
                QgsMapLayerRegistry.instance().addMapLayer(latlonLayer)
                generateFrames(latlonLayer, mapRect, 4000, 3000, mapCrs, elemCrs, -160000, 160000, -300000, 300000, GetFrameName5000);
            else:
                latlonLayer = QgsVectorLayer("Polygon", "2nd Mesh", "memory")
                QgsMapLayerRegistry.instance().addMapLayer(latlonLayer)
                generateFrames(latlonLayer, mapRect, 1.0/8, 1.0/12, mapCrs, elemCrs, -180, 180, -90, 90, GetFrameName2ndMesh);
        else:
            return

        symbol = QgsSymbolV2.defaultSymbol(QGis.Polygon)
        sLayer = QgsSimpleFillSymbolLayerV2(
                                            QColor.fromRgb(0, 0, 150), 
                                            Qt.NoBrush, 
                                            QColor.fromRgb(0, 0, 150), 
                                            Qt.SolidLine, 1.0 )
        sLayer = symbol.symbolLayer(0).clone()
        sLayer.setBrushStyle(Qt.NoBrush)
        sLayer.setBorderColor(QColor.fromRgb(0,0,150))
        sLayer.setBorderStyle(Qt.SolidLine)
        sLayer.setBorderWidth(1.0)
        symbol.changeSymbolLayer(0, sLayer)
        renderer = QgsSingleSymbolRendererV2(symbol)
        latlonLayer.setRendererV2(renderer)
        
        latlonLayer.enableLabels(True)
        label = latlonLayer.label()
        label.setLabelField(QgsLabel.Text, 0)
        labelAttr = label.labelAttributes()
        labelAttr.setColor(QColor.fromRgb(0, 0, 150))
        size = labelAttr.size()
        labelAttr.setSize(18.0, QgsLabelAttributes.PointUnits)
        
        self.canvas.refresh()
