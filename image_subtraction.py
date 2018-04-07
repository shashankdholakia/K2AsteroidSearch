#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Shashank Dholakia
"""
import os
import numpy as np
from astropy.io import fits

class ImageSubtraction:

   
    def main_image_subtraction(self,filepath):
        filelist = os.listdir(filepath)
        for filename in filepath
        hdulist = fits.open(filepath + '/' + filename)
        
            
        
    def load_single_image(self,filename):
        return hdulist
    
    def aligned_image(self,filename,reference):
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