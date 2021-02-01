from flask import request
from flask import redirect
from flask import render_template

from app.count.views import view

context = [
        [1, {'title': 'case 01', 'value': 0}],
        [2, {'title': 'case 02', 'value': 10}],
        [3, {'title': 'case 03', 'value': 5}],
        [4, {'title': 'case 04', 'value': 20}],
    ]


@view.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


@view.route('/count', methods=['GET', 'POST'])
def count():

    if request.method == 'POST':
        if request.args is not None:
            print(request.form.get('item'))
            # >>> START edit vaule
            index = request.args.get('index', type=int)
            value = request.args.get('value', type=int)
            item = request.args.get('item', type=str)

            if index is not None and value is not None:
                context[index-1][1]['value'] = value

            # working with forms
            if request.form is not None:
                index = request.form.get('index', type=int)
                value = request.form.get('value', type=int)
                item = request.form.get('item', type=str)
            # Redirct bad request

                # NEW ITEM
                if value is None:
                    value = 0
                if item is not None and item != '':
                    context.append([
                        len(context)+1,
                        {'title': item, 'value': value}
                        ])

                if index is not None:
                    indexs = []
                    for x in context:
                        indexs.append(x[0])
                    if index not in indexs:
                        return redirect('/count')

            if index is not None and value is not None:
                context[index-1][1]['value'] = value

            # >>> END edit value

    return render_template('count.html', context=context)
