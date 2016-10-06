#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
  
import cairo   
import pycha.pie
#import os
  
#设置画布  
def set_charvalue():  
    width,height=600,600   
    surface=cairo.ImageSurface(cairo.FORMAT_ARGB32,width,height)   
    return surface  
      
#画饼图  
def draw_pie(surface, options, dataSet, dir):  
    chart=pycha.pie.PieChart(surface,options)   
    chart.addDataset(dataSet)   
    chart.render()
    #os.system('rm -rf /srv/www/idehe.com/store/pie.png')
    surface.write_to_png(dir)  

if __name__ == "__main__":
    dataSet=(   
             ('iphone',((0,1),(0,0))),   
             ('htc',((0,4),(0,0))),   
            ) 
    options={   
            'legend':{'hide':False},   
            'title':'This is the title2',  
            'titleColor':'#0000ff',  
            'titleFont':'字体',  
            'background':{'chartColor': '#ffffff'},   
            'axis':{'labelColor':'#ff0000'},
            }
    surface = set_charvalue()  
    draw_pie(surface, options, dataSet)  
    
    
    
    
    