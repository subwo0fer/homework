def http_headers_to_json(ish_file_path, res_file_path):
    import json

    with open(ish_file_path) as f:
        c = f.readlines()
    d = {}

    if c[0].startswith('HTTP/1'):
        k = c[0].split(' ')
        d.update({'protocol':k[0]})
        d.update({'status_code':k[1].rstrip('\n')})
        buf_str = ''

        for i in range(2, len(k)):
            buf_str += k[i] + ' '
        d.update({'status_message':buf_str.rstrip('\n ')})

    elif c[0].startswith('HTTP/2'):
        k = c[0].split(' ')
        d.update({'protocol':k[0]})
        d.update({'status_code':k[1].rstrip('\n')})

    else:
        k = c[0].split(' ')
        d.update({'method':k[0]})
        d.update({'uri':k[1].rstrip('\n')})
        d.update({'protocol':k[2].rstrip('\n ')})

    c.pop(0)
    
    for v, line in enumerate(c):
        z = c[v].split(':')[0]
        x = c[v].lstrip(z + ':')
        x = x.lstrip()
        x = x.rstrip('\n')
        d.update({z:x})

    if d.get('\n') == '':
        d.pop('\n')
    with open(res_file_path, 'w') as f:
        json.dump(d, f, indent=4)
