# Leeds-Project
Computer Science Capstone Fall 2021 - Spring 2022

Data Sources (Sensitive -- not present in github. Reference refers to relative filepath on private repository)

1. Overview: Closed Caption Corpora (text) Data from 2012-2021 for the following six news networks: Fox News, FBC, CNN, CNBC, MSNBC, and Bloomberg.
   File Format: 56 (CSV) files. Bloomberg 2012 is not present.
   Size: Varies between 150 and 200 MB for each file.
   Content: Data is segmented by year and includes the text, title, and timestamps for every show that aired.
   Reference: Data/CorporaData/

2. Overview: CRSP Firm Name Data
   File Format: (CSV) file. 
   Size: 280 KB
   Content: Data includes stock tickers, official company name as listed on CRSP, and a unique identifier to search the CRSP database.
   Reference: Data/FirmNameData/firm.name.crsp.csv
 
3. Overview: CRSP Stock Market Data
   File Format: (CSV) file. 
   Size: 4 GB
   Content: Data includes daily stock price, volume, moving averages, volume weighted return, and P&L for every CRSP Firm Name from 2012-2021
   Reference: Data/Other/crspstocks.csv

4. Overview: The result of running Spacy Named Entity Recognition on the Closed Caption Corpora Data.
   File Format: 56 (CSV) files. Bloomberg 2012 is not present.
   Size: Varies between 10 and 20 MB for each file.
   Content: Spacy NER was modified to categorize entities by organizations, people, and other for each show that aired on Fox News, FBC, CNN, CNBC, MSNBC, and Bloomberg from 2012-2021.
   Reference: Data/MetaData/


Project Description: Studying captions from TV shows from major networks, with the idea of seeing their association with stock market movements, as well as studying the distribution of individuals mentioned (using spacy NER for people + Wikipedia to see who those people are) with the aim of uncovering potential political biases/narratives (from immigration to climate change and beyond).

Objective Statement: Develop software that provides actionable intelligence about market and media sentiment in real time while supporting the development of project management and NLP skills for the students.

Project Deliverables: Deliverables will be outlined in project charter and addendums, on a 4 week schedule of “sprints.” Each sprint will return a draft, a prototype, or a workable version, of a component of the final deliverable. Each sprint goal will be designed cooperatively between sponsor and the team, with approval/sign-off from both. Team signatures will be tracked with GoogleDocs version history and sponsor approval will be via email.


Methodology:

This Project Follows an Agile management strategy, where we work on sprints that vary in length from 2 weeks to one month. See folders for details regarding specific sprints.

1. Sprint-1 (9/17/21 -> 10/1/21)
2. Sprint-2 (10/22/21 -> 11/12/21)
3. Sprint-3 (11/14/21 -> 1/24/22) 
4. Sprint-4 (2/14/22 -> 3/2/22)
5. Sprint-5 (3/7/22 -> 3/24/22)
6. Sprint-6 (3/24/22 -> Now)
