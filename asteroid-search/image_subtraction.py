#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Shashank Dholakia
"""
import os
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS

"""

This subtracts images as described in Oelkers and Stassun 2018:
    https://arxiv.org/pdf/1803.02316



"""


class Image():
    
    """
    Contains a generic image's filename and filepath. Loading an image returns
    a HDUList object 
    
    """
    def __init__(filepath, filename):
        self.filepath= filepath
        self.filename = filename
        
    def load_image(self):
        if os.path.exists("directoryorfile")
            hdulist = fits.open(os.path.join(filepath, filename))
            return hdulist
        else:
            raise IOError("Input directory not found. Check that the path to the files really exists")

        
        
    
class TESSimage(Image):
    
    def __init__(self, filepath, filename):
        self.__init__(filepath,filename)
        self.year = int(filename[4:8])
        self.day = int(filename[8:11])
        self.hour = int(filename[11:13])
        self.minute = int(filename[13:15])
        self.second = int(filename[15:17])
        
        
    
class K2image(Image):
    
    def __init__(self, filepath, filename):
        self.__init__(filepath,filename)

    
class ImageSubtraction:

   
    def main_image_subtraction(self,filepath):
        filelist = os.listdir(filepath)
        for filename in filepath
        hdulist = fits.open(filepath + '/' + filename)
        
    
    
    def align_image(self,filename,ref_img):
        return hdulist
    
    def create_median_stacked_img(self,filepath):
        return hdulist
    
    def subtract_from_median(self,filename):
        return hdulist
    
    def find_background_threshold(self,filename):
        """find median and median absolute deviation of the image"""
        
        return background_threshold, sigma
        
    def create_bright_obj_mask(self,filename):
        """
        Takes a median-combined image and detects all bright pixels above a
        standard deviation cutoff in the image. Returns a mask (True/False array
        of all the regions in the image which are statistically significant pixels. 
        """
        
    def save_output():
        
if __name__ == '__main__':
    
    main_image_subtraction('/)