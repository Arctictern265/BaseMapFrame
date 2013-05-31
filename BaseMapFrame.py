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
from ui_selectSystem import Ui_DialogSelectSystem

class dlgSelectSystem(QDialog, Ui_DialogSelectSystem):
    
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.comboBox_system.addItem("I", QVariant(2443))
        self.comboBox_system.addItem("II", QVariant(2444))
        self.comboBox_system.addItem("III", QVariant(2445))
        self.comboBox_system.addItem("IV", QVariant(2446))
        self.comboBox_system.addItem("V", QVariant(2447))
        self.comboBox_system.addItem("VI", QVariant(2448))
        self.comboBox_system.addItem("VII", QVariant(2449))
        self.comboBox_system.addItem("VIII", QVariant(2450))
        self.comboBox_system.addItem("IX", QVariant(2451))
        self.comboBox_system.addItem("X", QVariant(2452))
        self.comboBox_system.addItem("XI", QVariant(2453))
        self.comboBox_system.addItem("XII", QVariant(2454))
        self.comboBox_system.addItem("XIII", QVariant(2455))
        self.comboBox_system.addItem("XIV", QVariant(2456))
        self.comboBox_system.addItem("XV", QVariant(2457))
        self.comboBox_system.addItem("XVI", QVariant(2458))
        self.comboBox_system.addItem("XVII", QVariant(2459))
        self.comboBox_system.addItem("XVIII", QVariant(2460))
        self.comboBox_system.addItem("XIX", QVariant(2461))
        self.comboBox_system.setCurrentIndex(8)
        self.radioButton_2500.setChecked(True)


def GetFrameName2500(x, y):
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


class BaseMapFrame(object):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()

    def initGui(self):
        self.action_genMesh = QAction(QIcon(":/icon/icon.png"), "BaseMapFrame", self.iface.mainWindow())
        self.iface.addToolBarIcon(self.action_genMesh)
        self.iface.addPluginToMenu(
            QCoreApplication.translate(
            "BaseMapFrame", "Creates Japan National Base Map Frame ..."), self.action_genMesh)

        QObject.connect(self.action_genMesh, SIGNAL("activated()"), self.genMesh)

    def unload(self):
        self.iface.unregisterMainWindowAction(self.action_genMesh)
        self.iface.removeToolBarIcon(self.action_genMesh)
        self.iface.removePluginMenu(QCoreApplication.translate(
            "BaseMapFrame", "Creates Japan National Base Map Frame ..."), self.action_genMesh)


    def checkExtent(self, rect, elemCrs, mapCrs):

        if rect.isEmpty():
            QMessageBox.information(self.iface.mainWindow(), "Warning",
                        QCoreApplication.translate("BaseMapFrame", "Map extent is empgy.") )
#                        QCoreApplication.translate("NationalBasicMesh", "%1 %2 %3 %4").arg(rect.xMinimum()).arg(rect.xMaximum()).arg(rect.yMinimum()).arg(rect.yMaximum()))
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

    def genMesh2500(self, layer, mapRect, elemCrs, mapCrs):

        trans = QgsCoordinateTransform(mapCrs, elemCrs)
        rect = trans.transform(mapRect)
        
        xmin = rect.xMinimum()
        ymin = rect.yMinimum()
        xmax = rect.xMaximum()
        ymax = rect.yMaximum()

        if rect.xMinimum() < -160000:
            rect.setXMinimum(-160000)
        if rect.xMaximum() > 160000:
            rect.setXMaximum(160000)
        if rect.yMinimum() < -300000:
            rect.setYMinimum(-300000)
        if rect.yMaximum() > 300000:
            rect.setYMaximum(300000)

        layer.startEditing()
        provider = layer.dataProvider()
        provider.addAttributes(
            [QgsField("MapName", QVariant.String)])
        y = (int(rect.yMinimum()) / 1500) * 1500
        while y < rect.yMaximum():
            x = (int(rect.xMinimum()) / 2000) * 2000
            while x < rect.xMaximum():
                f = QgsFeature()
                f.setGeometry(QgsGeometry.fromPolygon([[
                    trans.transform(QgsPoint(x, y), QgsCoordinateTransform.ReverseTransform),
                    trans.transform(QgsPoint(x, y + 1500), QgsCoordinateTransform.ReverseTransform),
                    trans.transform(QgsPoint(x + 2000, y + 1500), QgsCoordinateTransform.ReverseTransform),
                    trans.transform(QgsPoint(x + 2000, y), QgsCoordinateTransform.ReverseTransform),
                    trans.transform(QgsPoint(x, y), QgsCoordinateTransform.ReverseTransform)
                ]]))
            
                strFrame = GetFrameName2500(x, y + 1500)
            
                f.setAttributeMap({0: strFrame})
                layer.addFeature(f)
            
                x += 2000
            y += 1500
                        
        layer.commitChanges()
        layer.updateExtents()


    def genMesh5000(self, layer, mapRect, elemCrs, mapCrs):

        trans = QgsCoordinateTransform(mapCrs, elemCrs)
        rect = trans.transform(mapRect)

        if rect.xMinimum() < -160000:
            rect.setXMinimum(-160000)
        if rect.xMaximum() > 160000:
            rect.setXMaximum(160000)
        if rect.yMinimum() < -300000:
            rect.setYMinimum(-300000)
        if rect.yMaximum() > 300000:
            rect.setYMaximum(300000)

        layer.startEditing()
        provider = layer.dataProvider()
        provider.addAttributes(
            [QgsField("MapName", QVariant.String)])
        y = (int(rect.yMinimum()) / 3000) * 3000
        while y < rect.yMaximum():
            x = (int(rect.xMinimum()) / 4000) * 4000
            while x < rect.xMaximum():
                f = QgsFeature()
                f.setGeometry(QgsGeometry.fromPolygon([[
                    trans.transform(QgsPoint(x, y), QgsCoordinateTransform.ReverseTransform),
                    trans.transform(QgsPoint(x, y + 3000), QgsCoordinateTransform.ReverseTransform),
                    trans.transform(QgsPoint(x + 4000, y + 3000), QgsCoordinateTransform.ReverseTransform),
                    trans.transform(QgsPoint(x + 4000, y), QgsCoordinateTransform.ReverseTransform),
                    trans.transform(QgsPoint(x, y), QgsCoordinateTransform.ReverseTransform)
                ]]))
            
                strFrame = GetFrameName5000(x, y + 3000)
            
                f.setAttributeMap({0: strFrame})
                layer.addFeature(f)
            
                x += 4000
            y += 3000
                        
        layer.commitChanges()
        layer.updateExtents()


    def genMesh(self):
        
        dlg = dlgSelectSystem()
        if dlg.exec_() == QDialog.Accepted:
            
            systemNo = dlg.comboBox_system.itemData(dlg.comboBox_system.currentIndex()).toInt()[0]

            mapRenderer = self.canvas.mapRenderer()
            mapCrs = mapRenderer.destinationSrs()
            epsg = mapCrs.epsg()
            elemCrs = QgsCoordinateReferenceSystem()
            elemCrs.createFromEpsg(systemNo)
            mapRect = self.canvas.extent()
            
            if self.checkExtent(mapRect, elemCrs, mapCrs) == False:
                return
        
            if dlg.radioButton_2500.isChecked():
                latlonLayer = QgsVectorLayer("Polygon", "Base Map Frame 2500", "memory")
                QgsMapLayerRegistry.instance().addMapLayer(latlonLayer)
                self.genMesh2500(latlonLayer, mapRect, elemCrs, mapCrs)
            else:
                latlonLayer = QgsVectorLayer("Polygon", "Base Map Frame 5000", "memory")
                QgsMapLayerRegistry.instance().addMapLayer(latlonLayer)
                self.genMesh5000(latlonLayer, mapRect, elemCrs, mapCrs)
        
            QgsSymbologyV2Conversion.rendererV2toV1(latlonLayer)
        
            renderer = latlonLayer.renderer()
            symbol = renderer.symbol()
            symbol.setColor(QColor.fromRgb(0, 0, 150))
            symbol.setFillStyle(Qt.NoBrush)
            symbol.setLineStyle(Qt.SolidLine)
            lwidth = symbol.lineWidth()
            symbol.setLineWidth(1.0)

#        symbol = QgsSymbolV2.defaultSymbol(QGis.Polygon)
##        sLayer = QgsSimpleFillSymbolLayerV2(
##                                            QColor.fromRgb(0, 0, 150), 
##                                            Qt.NoBrush, 
##                                            QColor.fromRgb(0, 0, 150), 
##                                            Qt.SolidLine, 1.0 )
#        sLayer = symbol.symbolLayer(0)
#        sLayer.setBrushStyle(Qt.NoBrush)
#        sLayer.setBorderColor(QColor.fromRgb(0,0,150))
#        sLayer.setBorderStyle(Qt.SolidLine)
#        sLayer.setBorderWidth(1.0)
##        symbol.appendSymbolLayer(sLayer)
#        renderer = latlonLayer.rendererV2(symbol)
#        latlonLayer.setRendererV2(renderer)
        
            latlonLayer.enableLabels(True)
            label = latlonLayer.label()
            label.setLabelField(QgsLabel.Text, 0)
            labelAttr = label.layerAttributes()
            labelAttr.setColor(QColor.fromRgb(0, 0, 150))
            size = labelAttr.size()
            labelAttr.setSize(18.0, QgsLabelAttributes.PointUnits)
        
            self.canvas.refresh()
