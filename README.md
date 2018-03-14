# Labeled Health Tweets
This repo contains labeled tweets related to  various health conditions. 

## Purpose
This repor provides a file named labeledtweets.csv, which contains a list with 1,800 tweet ids and labels. Each tweet was collected with the Twitter API, and filtered to ensure it contains one of the following keywords:

1. flu
2. zika
3. diarrhea
4. ebola
5. measles

Each tweets was then labeled to determine if the topic was an actual disease or not. For example, the following 
tweet does not refers to a disease:

**Your idea is so bad, I think you have mental flu.**

In this case, the word flu is being used to emphasize that something was wrong with the someone's reasoning. 
On the other hand, the following tweet is about a disease: 

** My head is gonna explode thanks to my flu :( **

## Structure of the data
The dataset has a very simple structure. Each row consists of a tweet id, and a label. These two fields are 
separated by a commad. Due to the Twitter's licensing terms we cannot distribute the full text of the tweet.
However, we have included a file named getFullTweets that can be use to read the full tweet, including all 
its metadata. 

Each tweet was labeled by a group of stdents. There are two possible labels:

* 0 - the topic of the tweet is not a disease.
* 1 - the topic of the tweet is a disease.

