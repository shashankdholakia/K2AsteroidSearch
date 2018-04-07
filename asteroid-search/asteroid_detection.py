#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Shashank Dholakia
"""

import K2fov
from K2fov.projection import PlateCaree, HammerAitoff, Cylindrical
from K2fov import greatcircle
    
class TPF:
    """
    Represents a K2 Target Pixel File as 4 corners in RA and DEC and XYZ space
    
    """
    
    def __init__(self,corners):
        
        self.RA_DEC_corners = corners
        self.XYZ_corners = []
    def is_obj_in_TPF(self):
        ##computes shortest distance
        


        

class TPF_mosaic:
    
    """
    Represents the entire K2 footprint for a given campaign as a collection of 
    Target Pixel Files, each at a different position on the K2 camera chip
    """
    def __init__(self,campaign):
        self.campaign = campaign
        self.TPFs = [] #list of every TPF 
        
    def get_metdata(self):
        """Gets metadata from each K2 superstamp """
        
    def create_corners(self):
        """
        Accesses metadata file and finds corners of every TPF
        
        """
    def is_obj_in_TPFs(self,ra,dec):
        """
        
        """
        #object must be on silicon first to be within any TPFs!
        if not K2fov.isOnSilicon(ra, dec):
            return False
        
        for TPF in self.TPFs:
            if TPF.is_obj_in_TPF:
                return True
        #if object on silicon but not in any TPFs
        return False
        
class Asteroids:
    """
    Contains code for accessing the Minor Planet Database for the RA and DEC
    positions to look for asteroids that are in TPFs in a campaign of the K2
    mission
    """
    
    def __init__(self):
        
    def get_coords(self):
        """
        Accesses Minor Planet Database to get coordinates of every 
        asteroid in field of view
        """


    