#!/usr/bin/env python
# coding: utf-8

import boto3
from botocore.client import Config
from datetime import datetime
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
##### CONFIGURING PATHS & ZIPPING BACKUP FOLDER ########
########################################################

#Gives both time and date as a string==> datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
time_stamp = datetime.now().strftime("%I:%M%p_%d-%m-%Y")

#Appending the timestamp with the word "_backup" to uniquely identify the backup file
filename = time_stamp + "_backup" 

#Path to the directory whose contents will be archived so that it can be backed up to the s3 bucket
backup_dir = "/home/parth/Documents/automate_backup/back_up"

#Path to the file where the directory archived by shutil will be saved
filepath = '/home/parth/Documents/automate_backup/'+filename

#Path to the zip file that will be uploaded to the s3 bucket
backup_filepath = filepath + ".zip"

#The path in s3 bucket where the backupfile gets uploaded 
key_path = "kosh-es/"+filename+".zip"

#Used to archive the contents of the directory to be backedup
shutil.make_archive(filepath, 'zip', backup_dir)

########################################################
################ BACKING UP FILE #######################
########################################################

s3.meta.client.upload_file( backup_filepath, BUCKET_NAME, key_path)

#Create a method to update a specific text file with the name of the backupfiles
print(filename+".zip")

