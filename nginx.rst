.. _nginx:

nginx
=====

nginx is the main web server for Security Onion.

Configuration
-------------

You can modify nginx configuration by going to :ref:`administration` --> Configuration --> nginx.

.. image:: images/61_config.png
  :target: _images/61_config.png

Replacing Default Cert
----------------------

If you'd like to replace the default cert with your own cert, then you can do the following:

#. At the top of the page, click the ``Options`` dropdown menu and then enable the ``Show all configurable settings, including advanced settings.`` option.
#. On the left side, go to ``nginx``, and then expand ``ssl``.
#. Set ``Replace Default Cert`` to ``true``, and then click the checkmark to save the value.
#. Paste your cert file.
#. Paste your key file.

More Information
----------------

.. note::

    For more information about nginx, please see https://nginx.org/.
