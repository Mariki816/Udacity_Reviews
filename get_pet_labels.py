#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Marlene Hirose
# DATE CREATED: 2019-09-08                     
# REVISED DATE: 2019-09-18
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
        if not image.startswith("."):
        # Make sure image name is all in lower case, replace underscores with spaces. Use rsplit otherwise will split after first space. 
#         Create list that will only exist in this if statement
            image_list = []
        # split on period to get rid of jpg extension
            image_split_period = image.lower().split('.')

#            get rid of jpg from list
            image_split_period.pop()
            no_digits = []
        
#            get rid of numbers
            for elem in image_split_period:
                for char in elem:
                    if not char.isdigit():
                        no_digits.append(char)
                        
#             replace underscores with spaces and strip whitespaces
            image_name = ''.join(no_digits).replace( '_', ' ').strip(' ')         
#             add image name to the list
            image_list.append(image_name)
#             insert image name into dictionary
            if image not in results_dic:
                results_dic[image] = image_list

            else:
                print("** Warning: Duplicate files exist in directory:", image)

            # Replace None with the results_dic dictionary that you created with this
            # function

    return results_dic
