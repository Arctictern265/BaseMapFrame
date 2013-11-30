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

#import os, sys
#sys.path.append(r"C:\Program Files\eclipse\dropins\plugins\org.python.pydev.debug_1.6.3.2010100513\pysrc")
#import pydevd
#pydevd.settrace()  

def classFactory(iface):
    from BaseMapFrame import BaseMapFrame
    return BaseMapFrame(iface)
