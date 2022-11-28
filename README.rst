What is Memorio
==================

Memorio speeds up your functions execution by saving on disk their result when they are first called and reloading it the next time the function is called with the same input parameters. It is a valuable tool to speed up IA and machine learning projects developpement, where workflow have long runtime and many runs are necessary to mature it.

Cache is disable if the function or any nested subfunction called by the function has been changed between the last and the current run. This feature make it suited for developpement process.

It is especially relevant for function with long runtime and also suited for large input and output. 

Notable difference with existing libraries:

* functools's cache_lru: It is suited for small inputs and outputs, not large. It is not persistent and drops some cache when size limit is reached. It does not disable cache if the function or subfunction as changed.
* joblib's memorize: Although it disable cache when the function definition has changed, it does not check for subfunction change, which can lead to erroneous function return.

To avoid seeking change in external libraries, Memorio limits its scope to the current project (identified by a folder and all its subfolder). User are asked to keep it in mind when loading a more recent version of their external module or modifying them manually.

How does it work?
===================

First, import the module and crete an instance of Memorio

.. testsetup:: *

    from memorio import Memorio
    memorio = Memorio(cachedir)

To track a function IO, decorate it with memorio like this:

.. testcode::

    @memorio.cache
    def f(x):
        print('Running f({})'.format(x))
        return x
    
    f(1)
 
.. testoutput::
    
    Running f(1)

When the tracked function is called for the second time with the same input, it does not process the function but
returns the saved result.

.. doctest::

    >>> print(f(1))
    1
    