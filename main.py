import json
with open('data/NYSE_PEP.json') as data_file:
    res = json.load(data_file)
with open('result.js', 'w') as outfile:
    outfile.write("var json =")
    json.dump(res, outfile)
with open('data/NYSE_KO.json') as data_file:
    res = json.load(data_file)
print res["data"]
with open('result2.js', 'w') as outfile:
    outfile.write("var json2 =")
    json.dump(res, outfile)
