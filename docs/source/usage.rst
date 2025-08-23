Usage
=====

Start the API server:

.. code-block:: bash

   uvicorn app:app --reload

Open your browser or use ``curl``:

.. code-block:: bash

   curl "http://127.0.0.1:8000/api/scrape?query=headphones&limit=3"

Response:

.. code-block:: json

   [
       {
           "title": "Sony WH-1000XM4",
           "price": "$348.00",
           "rating": 4.7,
           "url": "https://www.amazon.com/dp/example"
       },
       ...
   ]
