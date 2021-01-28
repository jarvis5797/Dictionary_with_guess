from fuzzywuzzy import fuzz
import json , requests
data = json.loads(requests.get("https://raw.githubusercontent.com/jarvis5797/data_/master/data.json").text)
str=input()
a="Boy"
print(fuzz.ratio(str,a))
lst=[]
#for i in data:	
	#if fuzz.ratio(str,i)>85 and fuzz.ratio(str,i)<100:
		#lst.append(i)
	#if fuzz.ratio(str,i)==100:
		#print(i,data[i]
#if len(lst)>=1:
                #print("did you mean",lst)
