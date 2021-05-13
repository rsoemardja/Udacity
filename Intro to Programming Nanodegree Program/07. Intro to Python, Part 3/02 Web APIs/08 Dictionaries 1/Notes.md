>>> d = {'key1': 'value1'}
>>> d['key2'] = 'value2'
>>> d['key1']
'value1'
>>> d['key2']
'value2'
>>> d
{'key1': 'value1', 'key2': 'value2'}
>>> d['key2'] = 'foo'
>>> d['key2'] += 'bar'
>>> d['key2']
'foobar'
>>> d
{'key1': 'value1', 'key2': 'foobar'}