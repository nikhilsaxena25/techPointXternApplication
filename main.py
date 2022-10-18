from serpapi import GoogleSearch
import pandas as pd


def top_2(arr, n=2):
    temp = []
    count = 0
    for items in arr:
        if 'rating' in items:
            if items['rating'] >= 4.0 and count < n:
                temp.append(items)
                count += 1
    return temp


final_list = []
time_commit = []

params = {
    "engine": "google_maps",
    "q": "",
    "ll": "@39.7683331,-86.1583502,15.1z",
    "type": "search",
    "api_key": "a37967b7a90a0398dd74eb7c1a42f8c6a6aadccdeb7ff3a23132c024ef106c3a"
}

params['q'] = "fun things to do"
search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
final_list.append(top_2(local_results, 2))

params['q'] = "thai food"
search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
final_list.append(top_2(local_results, 1))

params['q'] = "shopping places"
search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
final_list.append(top_2(local_results, 2))

params['q'] = "chinese food"
search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
final_list.append(top_2(local_results, 1))

# print(final_list[0][0])
times = []
name = []
address = []
place_type = []
rating = []
website = []
phone = []

df1 = pd.DataFrame(columns=['Title', 'Activity_Type', 'Phone Number', 'Website', 'Rating', 'Address'])


def data_add(item):
    ret_list = []
    if 'title' in item:
        ret_list.append(item['title'])
    else:
        ret_list.append(None)

    if 'type' in item:
        ret_list.append(item['type'])
    else:
        ret_list.append(None)

    if 'phone' in item:
        ret_list.append(item['phone'])
    else:
        ret_list.append(None)

    if 'website' in item:
        ret_list.append(item['website'])
    else:
        ret_list.append(None)

    if 'rating' in item:
        ret_list.append(item['rating'])
    else:
        ret_list.append(None)

    if 'address' in item:
        ret_list.append(item['address'])
    else:
        ret_list.append(None)

    return ret_list


for items in final_list:
    for i in items:
        df1.loc[len(df1)] = data_add(i)

df1.insert(0, 'Time', ['9AM', '11AM', '2PM', '4PM', '6PM', '8PM'])
df1['Duration'] = ['2 hours', '3 hours', '2 hours', '2 hours', '2 hours', '1 hour']