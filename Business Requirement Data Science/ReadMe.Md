
Find the goal of the project. 
Identify the internal and external stakeholders
Ask the right questions. Such as how do this project add customers to the organization. 
Ask open ended questions and try to steer the discusstion towards the above goal.
Document this. 

Stakeholder need analysis: 
Provides project leaders access to stakeholder alliance, needs, intersts, knowledge of the data science project. 
Needs to be done at the begining of the project and supports better planning. 
Identify the impact of the stakeholders
Priortize the stakeholders in power and interest of the project
Is there sufficient knowledge and skill within the organization
Stop the process if no value is being delivered. Fail fast. 

data first extract
work with data analysist to identify key data sets that adds value to the project
extract the data 
clean and transform the data. remove outliers. 
perform basic alaysis keeping project need in mind. 
Use PaaS. 

Identify scope of data science project
Identify KPI. 
Sucess is when project has reached all KPI goals. 


Lifecycle of Data science project

OSEMN: Obtain data , Scrub data(clean data) , Explore data(find trends),Model(clean outliers), Interpret(if the model is robust enough then we move here).  

Quantify the risks. 

convert the impact of risk into numbers
perform risk assessment exercise.
make informed decision

Elements to consider: schedule, cost, performance, infrastructure. 
Risk mitigation: document alternatives, decrease likelihood. 

Pearson's R Correlation

## Non parametric Correlation Analysis

1. Spearman's Rank Correlation: works for ordianl variables

 assumes your variables are ordinal. i.e numeric , have set pair of values and able to be ranked like a categorical variable. The data is not related linearly and is non normally distributed.  Calculate value of R (Spearman's R Correlation Coefficient). 

    R = 1. Strong positive relationship 
    R = 0. no relationship
    R = -1. Strong negitive relationship


2. chi-square tables: 
    check non linear variables are independent of one another. 
    assumptions for chi-square
    your variables are categorical or numeric
    you have binned the numeric variables

    The H0 (Null Hypothesis): There is no relationship between variable one and variable two.

    The H1 (Alternative Hypothesis): There is a relationship between variable 1 and variable 2.

    Assumptions:

    When testing the data, the cells should be counts of cases and not percentages. It is okay to convert to percentages after testing the data
    The levels (groups) of the variables being tested are mutually exclusive
    Each participant contributes to only one cell within the Chi-square table
    The groups being tested must be independent
    The value of expected cells should be greater than 5 for at least 20% of the cells

    p>0.05 for variables to be independent of one another. IF not then reject the null hypothesis and say that variables are correlated. 

    Ordinal data:  In an ordinal scale, the levels of a variable are ordered such that one level can be considered higher/lower than another.  However, the magnitude of the difference between levels is not necessarily known.  An example would be rank ordering levels of education.  A graduate degree is higher than a bachelor’s degree, and a bachelor’s degree is higher than a high school diploma.  However, we cannot quantify how much higher a graduate degree is compared to a bachelor’s degree.  We also cannot say that the difference in education between a graduate degree and a bachelor’s degree is the same as the difference between a bachelor’s degree and a high school diploma.