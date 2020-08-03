# Format-Mapping
Based on similarity it map the fields, It takes on Source(input) and Target(output).

#API 1 : Supervised mode :
Input : Source and Target
Output : Source,Target with Mapping along with confidence score 

#API 2
Here trainer should check whether the Mapping is correct or incorrect :
Input :Source,Target and Mapping
Output : messege : Learned the mappings

#API 3 : UnSupervised mode :
Input : Source and Target
Output : Mapping with source to target fields

# Installing
pip install fuzzywuzzy

# API 1 - Matching in Supervised mode 
Goal: Map the source and target and find the confidence(ratio) of string match.
Using Levenshtein distan we call find the confidence of the mapping ratio.
Here i have used FUZZY logic, based on Levenshtein Distance the fuzzy logic works.

Input : Source and Target
Output : Source, Target and Mapping

#RunServer

Step 1 : Open the cmd 
C:\Users\abhinaychowdary.LENOVO-PC\Downloads\Mapping\map_field>py runserver.py

Step 2 : Open postman
https://github.com/AnushaBoyapati/Format-Mapping/issues/1#issue-671924492
#set all the felids as shown 
#link on the send ,it display an output


