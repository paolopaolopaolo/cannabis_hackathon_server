import requests


base_url = "https://api.calivahack.io"
products = "/products/v2/retail"
single_product = "/products/v2/retail/search"
api_key = {'apikey': 'Caliva420'}
search_location = "/locator/v2/storeLocator"
locations = "/locator/v2/stores"


class Caliva(object):

  def search_for_products(self, id=None, name=None):
    all_products = requests.get(base_url+products,  headers=api_key).json()
    results = []
    for _, category in all_products["data"].items():
      for _, item in category.items():
        results.append(item)
    return results


  def search_for_location(self, location=None):
    # search for a single location
    if location:
      payload = { "location": str(location)}
      location = requests.post(base_url+search_location, data=json.dumps(payload), headers= api_key)
    else:
      # returns all locations
      all_locations = requests.requests(base_url+locations, headers= api_key)
      for store in all_locations:
        return weed





