# Labeled Health Tweets
This repo contains labeled tweets related to  various health conditions. 

## Purpose
This repo provides a file named labeledtweets.csv, which contains a list with 1,800 tweet ids and labels. Each tweet was collected with the Twitter API, and filtered to ensure it contains one of the following keywords:

1. flu
2. zika
3. diarrhea
4. ebola
5. measles

Each tweet was then labeled to determine if the topic was an actual disease or not. For example, the following 
tweet does not refers to a disease:

**Your idea is so bad, I think you have mental flu.**

In this case, the word flu is being used to emphasize that something was wrong with the someone's reasoning. 
On the other hand, the following tweet is about a disease: 

**My head is gonna explode thanks to my flu :(**

The author of the tweet is complaining about felling ill due to the flu. 

## Structure of the data
The dataset has a very simple structure. Each row consists of a tweet id, and a label. These two fields are 
separated by a comma. Due to Twitter's licensing terms we cannot distribute the full text of the tweets.
The full text must be obtained directly from Twitter through their developers API. 
However, we have included a file named getFullTweets that can be use to read the full text in a tweet, including all 
its metadata. 

Each tweet was labeled by a group of students at the University of Puerto Rico, Mayaguez. 
There are two possible labels:

* 0 - the topic of the tweet is not a disease.
* 1 - the topic of the tweet is a disease.

Each tweet can labeled as belonging to one these classes. 

## How to get the data
In order to get the full text and metadata for each tweet you can use the program getFullTweets.py, which is 
a Python 3 application that we have included in this repo. You will also need to sign up for a free Twitter
developer account. The specific steps are as follows:

1. Clone this repo 
2. Sign up for a free Twitter developer account
3. Rename the file credentials-template.json as credentials.json
4. Modify the contents of credentials-template.json by adding your  credentials for your Twitter developer account.
5. Run the as follows: 

   python getFullTweets.py \<input file\> \<output file\>
  
   Parameters:
   * input file - file containing the tweet ids and labels
   * output_file - file cotaining the full text and metadata of each tweet. There is one record per line.
   
## Acknowledgements
This work was completed by a set of graduate and undergraduate students at the University of Puerto Rico, Mayaguez:  
1. Andres Hernandez
2. Jady Urbina
3. Cristian Garzon
4. Danny Villanueva
5. Luis G. Rivera
6. Juan Cabrera

Research reported in this publication was supported by the National Library of Medicine, of the National Institutes of Health under award number R15LM012275. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

## Licenses 

The content of this project itself is licensed under the [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/), and the underlying source code used to collect the tweets is licensed under the 
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
