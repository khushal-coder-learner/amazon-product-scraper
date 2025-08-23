Amazon Product Scraper Documentation
====================================

Welcome to the documentation for **Amazon Product Scraper** –  
a lightweight API that extracts structured product details from Amazon search results.  

This project was built with **Python** and **Flask**, and is designed to be both  
simple to use and easy to extend.  

Overview
--------

The scraper provides:

- A clean **REST API** for querying Amazon products
- Fields such as **title, price, rating, reviews, URL**
- Optional parameters like ``limit`` to control number of results
- JSON output for easy integration with apps, scripts, or dashboards
- A modular design for extending scraping logic

Who is this for?
----------------

- **Developers** who need structured Amazon product data
- **Data Analysts** exploring pricing or rating trends
- **Students & Learners** practicing API development & web scraping
- **Portfolio Projects** to showcase coding + documentation skills

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Sections

   installation
   usage
   api
   contributing
   faq
   changelog

Quick Example
-------------

A quick request to scrape laptops from Amazon:

.. code-block:: bash

   curl "http://127.0.0.1:8000/api/scrape?query=laptop&limit=5"

Sample JSON response:

.. code-block:: json

   [
       {
           "title": "Dell Inspiron 15",
           "price": "$549.99",
           "rating": 4.3,
           "url": "https://www.amazon.com/dp/example"
       }
       // more results here
   ]

Support & Contributions
-----------------------

If you encounter issues, please check the **FAQ** or open an issue  
on the project’s GitHub repository.

Contributions are welcome! See the ``contributing`` page for guidelines.

License
-------

This project is released under the MIT License.  
See the ``LICENSE`` file in the repository for details.
