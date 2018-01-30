from bottle import get, post, delete, request, run
import collections, json

if __name__ == "__main__":
  store = collections.defaultdict(str)
  
  @get("/")
  def _alive():
    o = {"status": "active"}
    return json.dumps(o)

  @get("/dict")
  def _dict():
    return json.dumps(store)

  @post("/update")
  def _add():
    req = json.load(request.body)
    store.update(req)
    return json.dumps(store)
    
  run(host="0.0.0.0", port=8080)

