API Reference
=============

Scraper Functions
-----------------

.. automodule:: scraper.scraper
   :members:
   :undoc-members:
   :show-inheritance:

API Endpoints
-------------

**GET /api/scrape**

Query Amazon products by keyword.

Parameters:

- ``query`` (*str*): The search term (required).
- ``limit`` (*int*, optional): Number of results. Default = 10.

Example:

.. code-block:: bash

   curl "http://127.0.0.1:8000/api/scrape?query=laptop&limit=5"
