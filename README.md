opps-documents
================
Sent your Documents into a Post or any Container.


Installation
-------------

Install the opps-documents lib:
```
python setup.py install
```

or
```
pip install opps-documents
```


Configuration
-------------

Include opps.documents on your django settings
```python
INSTALLED_APPS += (
    'opps.documents',
)
```

Create DB tables:
```
python manage.py syncdb
```

License
=======

Copyright 2014 `YACOWS <http://yacows.com.br/>`_. and other contributors
