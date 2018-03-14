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

Your idea is so bad, I think you have mental flu. 

In this case, the word flu is being used to emphasize that something was wrong with the someone's reasoning. 
On
