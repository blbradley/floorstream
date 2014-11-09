floorstream
===========

Python API for working with custom dance floor


Requirements
------------

* Python 2.7.x (latest plz)


Development
-----------

* Setup a virtualenv
* `python setup.py develop`

Usage
-----

        from floorstream import Floor

        floor = Floor(host, port)
        floor.connect()

        data = [[0, 0, 255] for i in xrange(64)] # solid blue
        floor.send(data)
