def hello(env, start_response):
    query = env['QUERY_STRING']
    ret = bytes('\n'.join(query.split('&')), 'UTF8') + b'\n'
    print('1')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return iter([ret])
