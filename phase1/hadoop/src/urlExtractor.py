import json

#loading json data
try:
    json_data = []
    for json_object in open("out.json", 'r', encoding='utf-8'):
        json_data.append(json.loads(json_object))
except:
    print('Error could not load json object')

#Writing the extracted into a file called urls.txt
with open("urls.txt", "w+", encoding='utf-8') as f:
    for i in range(len(json_data)):
        hashtags=json_data[i]["entities"]['hashtags']
        urls_object=json_data[i]["entities"]['urls']
        location=json_data[i]["user"]['location']

        h=len(hashtags)
        uo=len(urls_object)
        q=len(location)
        
        if h!=0:
            for j in range(h):
                f.write(hashtags[j]["text"] +"\n")
        elif uo!=0:
            for k in range(uo):
                f.write(urls_object[k]["url"] +"\n")
            for l in range(uo):
                f.write(urls_object[l]["expanded_url"] +"\n")
        elif q!=0:
                f.write(location+"\n")