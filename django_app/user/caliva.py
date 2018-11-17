import requests
import pprtint

base_url = "https://api.calivahack.io"
products = "/products/v2/retail"
single_product = "/products/v2/retail/search"
api_key = {'apikey': 'Caliva420'}
search_location = "/locator/v2/storeLocator"
locations = "/locator/v2/stores"


class Caliva(object):

  def search_for_products(id=None, name=None):
    # search for a single product by id
    product_id = f"/{id}"
    if product_id:
      all_weed = requests.get(base_url+products+product_id,  headers= api_key)
      for ganja in all_weed:
        return ganja
    else:
      # search for a single product name string
      if name:
        payload = { "search": str(name)}
        product = requests.post(base_url+single_product, data=json.dumps(payload), headers= api_key)
      else:
        # returns all products
        all_products = requests.get(base_url+products,  headers= api_key)
        for weed in all_products:
          return weed

  def search_for_location(location=None):
    # search for a single location
    if location:
      payload = { "location": str(location)}
      location = requests.post(base_url+search_location, data=json.dumps(payload), headers= api_key)
    else:
      # returns all locations
      all_locations = requests.requests(base_url+locations, headers= api_key)
      for store in all_locations:
        return weed





