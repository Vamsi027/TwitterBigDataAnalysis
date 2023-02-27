# TwitterBigDataAnalysis

The repository stores project files related to Big Data.
Phase 1 of the project has been commited and its details are mentioned below.

In the initial phase 1, have executed word count program in both hadoop and spark on extractd twitter data.

The phase 1 folder structure is as follows

**1.[hadoop](https://github.com/Vamsi027/TwitterBigDataAnalysis/tree/main/phase1/hadoop):-**  \
           This is one of the directories in this we have two sub directories src and logs.\
           The logs of the word count program are stored in the logs folder.\
           The src folder consists of a python program to extract out.json file into urls.txt.\
           out.json consists of twitter data in the form of json objects.\
           Within urls.txt we have extracted hashtags,urls,expanded_urls and location of each tweet.\
           And finally had to run this cmd (hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.1.jar wordcount "sourcepath" "destinationpath") to get the word count output stored in part-r-00000 file.\
**2.[spark](https://github.com/Vamsi027/TwitterBigDataAnalysis/tree/main/phase1/spark/src):-**  \
           This is one of the directories in this we have only the src folder.\
           The src folder consists of a python program to extract out.json file into urls.txt.\
           out.json consists of twitter data in the form of json objects.\
           Within urls.txt we have extracted hashtags,urls,expanded_urls and location of each tweet similar to the above hadoop src folder until now.\
           And finally had to run this cmd ($SPARK_HOME/bin/spark-submit run-example JavaWordCount "sourcepath") to get the word count output stored in wordCountSpark.txt file.\
