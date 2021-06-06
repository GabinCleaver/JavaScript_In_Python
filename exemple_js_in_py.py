import js2py

js1 = 'console.log( "Hello World!" )'

res1 = js2py.eval_js(js1)
res1

a = int(input('Saisissez un numéro : '))
js2 = '''function add(a, b){
    return a + b;
    }'''
    
res2 = js2py.eval_js(js2)

print(res2(a,3))