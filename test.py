# Paul Shen
# www.karenina.io
# pxshen@alumni.stanford.edu
# 650-924-9206

import requests
import time

KEY = __MY_KEY__
l = [
    ('我的中国文是很坏', 'zh'),
    ('me no pueder hablars bueno espanio', 'es'),
]

# supported languages: en, es, fr, 中文
for q, lang in l:
    # model works best between these lengths. larger texts can be split and fed in parallel
    # assert len(q) > 50
    assert len(q) < 500

    start = time.time()
    # query gateway server
    r = requests.post('https://us-central1-project-318531836785902414.cloudfunctions.net/karenina',
                      json={
                          'q': q,
                          'lang': lang,
                          'key': KEY,
                      }).json()
    dt = time.time() - start
    print(f'elapsed time: {dt}')

    print(r)
    if 'error' not in r:
        pass
        # run precision/recall metrics on
        # r['input']
        # r['output']
