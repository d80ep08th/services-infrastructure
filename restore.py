#!/usr/bin/env python
# coding: utf-8

import os 
import boto3
from botocore.client import Config
import shutil

########################################################
############### AWS s3 BUCKET CONFIGURATION ############
########################################################

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = ''

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

########################################################
############ FILE & PATH CONFIGURATION #################
########################################################

#Get the name of the backup file to be downloaded from the s3 bucket
filename = input("Enter name of the backup file <timestamp>_backup.zip ==>")


#Path to the directory where you want to download the named file
parent_dir =  "/home/parth/Documents/automate_backup/restore/"

#The path in s3 bucket where the backupfile gets downloaded from 
key_path = "kosh-es/" + filename

#Path to the zip file on the local machine where the backup file is restored
restore_path =  parent_dir + filename

########################################################
################ RESTORING FILE ########################
########################################################
 
s3.meta.client.download_file(BUCKET_NAME, key_path, restore_path)

########################################################
########### EXTRACT RESTORED ZIP FILE ##################
########################################################

# will remove '.zip' from the filename to create a 
# directory with the same name and unpack the content 
# of the zip file in that directory

extract_dir = restore_path[:-4]
os.mkdir(extract_dir)

shutil.unpack_archive(filename, extract_dir, "zip")
