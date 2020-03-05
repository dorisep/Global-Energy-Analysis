# Understanding Energy Production & Consumption Trends
 Demonstrating the relationship between economic growth and energy consumption

#### -- Project Status: [Completed]

## Project Intro/Objective
Understanding Energy Production & Consumption Trends in Countries|Cities Across The World & Its Relationship With Relative Economic Growth Over the Last Two Decades. 

### Methods Used
* Data Collection
* API
* Web Scraping
* NoSQL database
* Data Cleaning
* Data Analysis
* Data Interpretation
* Data Visualization

### Technologies
* Python libraries:
    * pandas
    * requests
    * pymongo
    * BeautifulSoup
    * OS
    * flask
* JavaScript
    * D3
    * JQuery
    * HighChartJs
* HTML
* CSS
    * Bootstrap

## Project Description
* Data sets:
    * Kaggle
        * Olympic Medal Data - csv
        * World Marathon Majors - csv
     * World Bank
        * GDP Data - csv
    * CIA World Book - JSON dump
    * World Weather Online - API call

The project started by exploring 100 years of Olympic marathon medal data in which the sudden rise and pronounced success of two African nations, Ethiopia and Kenya, was of interest. Many secondary sources were encountered where journalists and acedemics had looked into this. However, there was little to no data involved in their analysis. Consistent in the hyposthesis found in these sources were interests in the influence of demographics and benefit of climate and geography in training. 

Initially there were challenges in cleaning the Olympic data, isolating the Marathon results, merging this with the data from the World Marathon Majors and standardizing labels and metrics. In order to collect the pertinent demographic data for each of the countries a JSON dump from the CIA World Book was sourced. In order to collect climate data an API call was utlized to gather 5 years of weather data for cities that held either major races or the olympics. The weather data for the African countries was approximated by refrencing their respective capital cities.

## Needs of this project

- data exploration/descriptive statistics
- app construction - api and webscrapping
- building database
- web page construction
- data processing/cleaning
- data visualization
- writeup/reporting

## Getting Started

1. Clone this repo: https://github.com/dorisep/Marathon_Analysis_Project.git 

    (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).

2. Raw Data is being kept [here](https://github.com/dorisep/Marathon_Analysis_Project/tree/master/Data) within this repo.

* offline data for Jonathan_Project01.ipynb
    *[athlete_events.csv](https://www.kaggle.com/itsfarhan/athletes-events-datasets) 
    *[Female_Elite_Berlin.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Female_Elite_Berlin.csv)
    *[Female_Elite_Boston.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Female_Elite_Boston.csv)
    *[Female_Elite_Chicago.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Female_Elite_Chicago.csv)
    *[Female_Elite_London.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Female_Elite_London.csv)
    *[Female_Elite_New_York.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Female_Elite_New_York.csv)
    *[Female_Elite_Tokyo.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Female_Elite_Tokyo.csv)
    *[Male_Elite_Berlin.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Male_Elite_Berlin.csv)
    *[Male_Elite_Boston.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Male_Elite_Boston.csv)
    *[Male_Elite_Chicago.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Male_Elite_Chicago.csv)
    *[Male_Elite_London.csv](https://www.kaggle.com/itsfarhan/athletes-events-datasets)
    *[Male_Elite_New_York.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Male_Elite_London.csv)
    *[Male_Elite_Tokyo.csv](https://www.kaggle.com/gjbroughton/world-marathon-majors#Male_Elite_Tokyo.csv)

* offline data for project1_GDPVsMedals.ipynb
    *[athlete_events.csv](https://www.kaggle.com/itsfarhan/athletes-events-datasets)
    *[API_NY.GDP.MKTP.CD_DS2_en_csv_v2_103640.csv](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)

* offline data for GroupProject.ipynb
    * uses major_marathon_men.csv and major_marathon_women.csv from Jonathan_Project01.ipynb
    * uses gdp_data from project1_GDPVsMedals.ipynb

3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)

## Featured Notebooks/Analysis/Deliverables
* [Notebooks](https://github.com/dorisep/Marathon_Analysis_Project/tree/master/Jupyter%20Notebooks)
* [Data Visualizations](https://github.com/dorisep/Marathon_Analysis_Project/tree/master/Data%20Visualizations)
* [Written Analysis](https://github.com/dorisep/Marathon_Analysis_Project/blob/master/Summary:Presnetation/PyKnot%20-%20Going%20the%20Distance_%20Summary%20(1).pdf)
* [Presentation](https://github.com/dorisep/Marathon_Analysis_Project/blob/master/Summary:Presnetation/Case%20study.pdf)


## Contributing Members

Taiwo Onitiri|[github](https://github.com/tonitiri)|[LinkedIn](https://www.linkedin.com/in/taiwo-onitiri-05479437/)|

* GroupProject.ipynb
* Written Analysis

Edward Doris|[github](https://github.com/dorisep)|[LinkedIn](https://www.linkedin.com/in/eddoris/)|

* CIA_WFB_Json.ipynb
* Historical_majors_weather.ipynb
* Written analysis/final edit
* Presentation