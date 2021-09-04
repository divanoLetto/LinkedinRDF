# Linkedin Web Scraping: creating a ontology for Sematic Web 
## Authors: Lorenzo Mandelli
#### Università degli Studi di Firenze

---

The project allows to extract data from the __Linkedin__ application through a Data Scraping phase and subsequently through them populate a structured __RDF graph__ starting from an ontology that summarizes the functional scheme of the famous working application.
To achieve this objective, the extracted data are converted into a structure compatible with an __Insert query__ expressed in the __SPARQL__ language and are then inserted into the RDF model through the use of the TopBraidComposer application which allows the operation.
The resulting RDF graph, also available at the address, allows in its limited size the use of queries in SPARQL for the purposes of statistical analysis.

![Ontology Schema](images/OntSchema.png "Ontology schema")

---

## Installation

This code was written in Python 3.8. The Selenium library is required for the Data Scraping phase and it can be obtained through *pip install selenium*.

## Usage

In order to run the program execute the file *main.py*. 
For the execution it is required that the google browser window used for the web scraping phase is not minimized for the entire duration of the application.

In order to provide login credentials to Linkedin for viewing profiles, the following account has been made available: * "bryansevendeadlysins@outlook.com" *, password = * "Arthur123" *.

In the event of a high number of accesses to the Linkedin account, it may be required to resolve a captcha in order to start the application correctly.