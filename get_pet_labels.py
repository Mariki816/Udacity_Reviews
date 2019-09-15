#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Marlene Hirose
# DATE CREATED: 2019-09-08                     
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    dir_list = listdir(image_dir)
#     print("Files and directories in '", image_dir, "' :")  
    # print the list 
#     print(dir_list)
    results_dic = {}
    image_name = ""
    for image in dir_list:
#         print(image)
        
    # Make sure image name is all in lower case, replace underscores with spaces. Use rsplit otherwise will split after first space. We want
    # split on last space
        image_split = image.lower().replace('_', ' ').rsplit(None, 1)
#         print(image_split)
#     Don't want the latter half - the numbers and jpg suffix. So, just get the first half of the split
#         image_name = image_split
        if image not in results_dic:
            results_dic[image] = image_split
#           Only want the lable, not the numbers and jpg
            results_dic[image].pop()
        else:
            print("** Warning: Duplicate files exist in directory:", image)
#     print(results_dic)
        # Replace None with the results_dic dictionary that you created with this
        # function
        
    return results_dic
