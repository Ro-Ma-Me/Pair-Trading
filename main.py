from utils import *
from web import *
import web

urls = (
    '/', 'index',
    '/generate', 'generate'
)
render = web.template.render('templates/')
template = web.template.render('templates/')

app = web.application(urls, globals())

def my_form(form_input=None):
    """
    Generate form with web.py
    """

    # from POST
    if form_input:
        myform = form.Form(
            form.Dropdown('Stock1', ['KO', 'PEP', 'CVX', 'XOM'], value=form_input.Stock1),
            form.Dropdown('Stock2', ['KO', 'PEP', 'CVX', 'XOM'], value=form_input.Stock2),
            form.Dropdown('Years', ["1","2","3","4"], value=form_input.Years))
    # from GET
    else:
        myform = form.Form(
            form.Dropdown('Stock1', ['KO', 'PEP', 'CVX', 'XOM']),
            form.Dropdown('Stock2', ['KO', 'PEP', 'CVX', 'XOM']),
            form.Dropdown('Years', ["1","2","3","4"])
            )

    return myform


class index:
    def GET(self):
        form = my_form()
        return render.index(form, None, 6)

    def POST(self):
        post_input = web.input(_method='post')
        form = my_form(post_input)
        numberOfYears = int(post_input.Years) if post_input.Years else 1
        lol = correlation(post_input.Stock1, post_input.Stock2, numberOfYears)
        return render.index(form, lol, numberOfYears + 1)


class generate:
    def GET(self):
        crawl()


if __name__ == "__main__":
    app.run()
