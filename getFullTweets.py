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