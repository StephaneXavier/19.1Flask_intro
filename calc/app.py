from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    # args come back as strings
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # must post back as string
    return str(operations.add(a,b))


@app.route('/sub')
def sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operations.sub(a,b))

@app.route('/mult')
def mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operations.mult(a,b))

@app.route('/div')
def div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operations.div(a,b))
# *************************************
# *************************************
# **************************************

@app.route('/math/<operation>')
def find_operation(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    if operation == 'add':
        return str(operations.add(a,b))
    if operation == 'sub':
        return str(operations.sub(a,b))
    if operation =='mult':
        return str(operations.mult(a,b))
    else:
        return str(operations.div(a,b))
# ******************************
# these 2 bits of code do the same thing 
# ******************************
operators = {
    # these are the funcs called from other file
    "add": operations.add,
    "mult":operations.mult,
    "div":operations.div,
    "sub":operations.sub
}

@app.route('/math/<oper>')
# the dynamic <> needs to be passed as ar in func
def do_math(oper):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(operators[oper](a,b))



