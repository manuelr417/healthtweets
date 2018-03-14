#
# Copyright (c) 2018 - University of Puerto Rico, Mayaguez
# Author: Andres Hernandez - andres.hernandez2@upr.edu
# Project: Twitter Health Surveilance (THS)
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, 
# software distributed under the License is distributed on an 
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
# either express or implied. See the License for the specific 
# language governing permissions and limitations under the License.
#
from twitter import Twitter, OAuth
import json
import sys
import time


def read_credentials():
    file_name = "credentials.json"
    try:
        with open(file_name) as data_file:
            return json.load(data_file)
    except:
        print ("Cannot load "+ data_file)
        return None

# Program assumes input file in form tweet_id|some_text
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Incorrect number of arguments. Usage: getFullTweets.py <input file> <output file>")
    credentials = read_credentials()
    t = Twitter(auth=OAuth(credentials['ACCESS_TOKEN'], credentials['ACCESS_SECRET'], credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET']))
    inputFile = open(sys.argv[1], "r")
    outputFile = open(sys.argv[2], "a")
    print("Starting to get tweets")
    start = time.time()
    count = 0
    for line in inputFile:
        if count >= 900:
            while (time.time() - start < 900):
                time.sleep(5)
            count = 0
            start = time.time()
        line = line.split("|")
        if line[0].isdigit():
            try:
                tweet = t.statuses.show(tweet_mode="extended",id=line[0])
                outputFile.writelines(json.dumps(tweet) + "\n")
                print(count)
            except:
                print("There was an error with tweet id=" + line[0])
            count += 1
    outputFile.close()
    inputFile.close()
