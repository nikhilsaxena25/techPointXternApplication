from serpapi import GoogleSearch

params = {
  "engine": "google_maps",
  "q": "pizza",
  "ll": "@39.7683331,-86.1583502,15.1z",
  "type": "search",
  "api_key": "a37967b7a90a0398dd74eb7c1a42f8c6a6aadccdeb7ff3a23132c024ef106c3a"
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
print(local_results[0])
