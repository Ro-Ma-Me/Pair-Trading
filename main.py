import json
import time
import requests
import urlparse
from scipy.stats.stats import pearsonr
import web
from web import form

urls = (
    '/', 'index',
    '/generate', 'generate'
)
render = web.template.render('templates/')
template = web.template.render('templates/')

app = web.application(urls, globals())

myform = form.Form(
    form.Dropdown('Stock1', ['KO', 'PEP', 'CVX', 'XOM']),
    form.Dropdown('Stock2', ['KO', 'PEP', 'CVX', 'XOM']),
    form.Textbox('Years'))

def correlation(stock1,stock2,**keyword_parameters):
    if ('optional' in keyword_parameters):
        numberOfYears = keyword_parameters['optional']
        numberOfDays = int(numberOfYears * 251 )
    else:
        numberOfYears = 15
        numberOfDays = 0
    fileToOpen = "data/" + stock1 + ".json"
    fileToOpen2 = "data/" + stock2 + ".json"
    data1 = []
    data2 = []
    with open(fileToOpen) as data :
        res = json.load(data)
        for i in range (len(res["dataset"]["data"]) - numberOfDays,len(res["dataset"]["data"])):
            data1.append(res["dataset"]["data"][i][1])
        data.close()
    with open(fileToOpen2) as data :
        res = json.load(data)
        for i in range (len(res["dataset"]["data"]) - numberOfDays,len(res["dataset"]["data"])):
            data2.append(res["dataset"]["data"][i][1])
        data.close()
    return "Correlation of the stocks " + stock1 + " and " + stock2 + " for the last " + str(numberOfYears) + " year(s) is : " + str(pearsonr(data1,data2)[0])

class generate:
    def GET(self):
        pattern = '%Y-%m-%d'
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
        }
        stocksToCrawl = ["KO",'PEP',"XOM","CVX"]
        URLToFill  = "https://www.quandl.com/api/v3/datasets/YAHOO/{0}.json?auth_token=hTQ-bA6dx-uV2EKM6X8S&column_index=4&order=asc&start_date=2000-10-13"
        for stock in stocksToCrawl:
            urlFinal = URLToFill.format(stock)
            fileToCreate = "data/" + stock + ".json"
            page = requests.get(urlFinal, headers=headers)
            with open(fileToCreate, 'w') as outfile:
                outfile.write(page.content)
                outfile.close()
            with open(fileToCreate) as data_file:
                res = json.load(data_file)
            for i in range (0,len(res["dataset"]["data"])):
                res["dataset"]["data"][i][0] = int(time.mktime(time.strptime(res["dataset"]["data"][i][0], pattern)))*1000
            fileResults = "static/js/" + stock + ".js"
            with open(fileResults, 'w') as outfile:
                outfile.write("var json" + stock +  "=")
                json.dump(res, outfile)

class index:
    def GET(self):
        correlation("KO","PEP",optional = 1)
        correlation("KO","PEP",optional = 2)
        correlation("KO","PEP",optional = 3)
        correlation("KO","PEP",optional = 4)
        form = myform()
        return render.index(form, None)

    def POST(self):
        form = myform()
        post_input = web.input(_method='post')
        numberOfYears = int(post_input.Years) if post_input.Years else 1
        lol = correlation(post_input.Stock1,post_input.Stock2,optional = numberOfYears)
        return render.index(form, "dsdsqdq")

if __name__ == "__main__":
    app.run()
