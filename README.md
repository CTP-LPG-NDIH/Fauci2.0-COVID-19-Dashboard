# COVID-19 Dashboard

COVID-19 virus permeates the lives of many in the United States where the case counts are difficult to understand at face value. We investigated what are the possible factors that may contribute to case growth across the United States. Factors including volume of international airports, mask usage by county, and population by state. Currently we are visualizing these factors and interpreting the relationships between these factors and the case growth.


## Deployed Webapp

https://covid19db2468.herokuapp.com

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Install flask

```
pip install Flask==1.1.1
```

Install the following plotly libraries using pip 

```
pip install plotly==4.13.0
pip install dash==1.18.0
pip install dash-bootstrap-components==0.10.7
pip install dash-core-components==1.14.0
pip install dash-html-components==1.1.1
pip install dash-renderer==1.8.3
pip install dash-table==4.11.1

```

Install pandas

```
pip install pandas==0.25.1
```

Install numpy

```
pip install numpy==1.17.0
```


### Cloning Repo

Clone the repo with the following command in git bash or you can download it directly from the repo
```
git clone https://github.com/CTP-LPG-NDIH/Fauci2.0-COVID-19-Dashboard.git
```

### Running the web app locally

Access the repo using command prompt. In your terminal, change the directory a folder named **dashapp**
```
cd dashapp
```

Running the webapp
```
ipython app.py
```


## Built With

* [Dash](https://dash.plotly.com/introduction) - The web framework used
* [Plotly](https://plotly.com/) - Graphing library used
* [Heroku](https://www.heroku.com/) - Deployment


## Authors

* **Isaiah Hong** - [Github](https://github.com/Isaiahhonggitws126)
* **Nicholas Dropp** - [Github](https://github.com/ndropp92)

See also the list of [contributors](https://github.com/CTP-LPG-NDIH/Fauci2.0-COVID-19-Dashboard/graphs/contributors) who participated in this project.


