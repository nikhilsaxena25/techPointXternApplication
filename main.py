from serpapi import GoogleSearch


def top_2(arr, type):
    temp = []
    count = 0
    for items in arr:
        if items[type] >= 4.0 and count < 2:
            temp.append(items)
            print(items)
            count += 1
    return temp


final_list = []
time_commit = []

params = {
    "engine": "google_maps",
    "q": "fun things to do",
    "ll": "@39.7683331,-86.1583502,15.1z",
    "type": "search",
    "api_key": "a37967b7a90a0398dd74eb7c1a42f8c6a6aadccdeb7ff3a23132c024ef106c3a"
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
final_list.append(top_2(local_results, "rating"))

params['q'] = "thai food"
search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
final_list.append(top_2(local_results, "rating")[0])
#
params['q'] = "shopping places"
search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
#print(local_results[0])
final_list.append(top_2(local_results, "rating")[0])
