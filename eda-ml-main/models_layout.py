from dash import html
from dash import dcc
from app import div_style

# machine learning
text_chunk1 = """

### Models
As seen in the Models Info tab, our best model is XXXXXXX. We use this model for our predictions for income in the future. You can change the following variables: XXXXXXXXXXX.

"""

text_chunk2 = """
#### Models Info

XXXXXXXXXXX
"""

text_chunk3 = """
#### Summary

We fit a total of 5 statistical models: linear regression, lasso regression, elastic net, generalized additive model, and XGBoost. Our dependent variable was INCOME.


We used MSE and R^2 values to compare each of our models and evaluate them. We start with our summary table and go into detail on the specifications for each of our models below:


|  |Linear Regression | Lasso Regression| Elastic Net | GAM | XG Boost |
| --- | --- | --- | --- | --- | --- |
| MSE |  |  |  |  |  |
| R-squared |  |  |  |  |  |

"""

text_chunk4 = """
#### Independent Variables

We were interested in exploring social determinants of income, or societal factors that may have a strong association with income. Therefore, we began with a wide array of different societal factors. We used our EDA to help us narrow down the variables for our models by choosing the factors that seemed to have the strongest associations with income. For example, our EDA showed that education and income was highly correlated. Additionally, we saw that because of inflation, the year variable was also highly correlated with income. Using this logic, we used the following independent variables we thought could have a strong association with income, both based on our prior knowledge and our EDA:

-   YYYY: The year the income was recorded on the survey.

-   AGE: The age of the respondent in any given year.

-   MARRY: The marital status of the respondent in any given year.

-   ECLGRD: Does the respondent have a college degree?

-   BAGO: Does the respondent think that at the present time business conditions are better or worse than they were a year ago?

-   BEXP: Does the respondent think that next year business conditions are better or worse than they were a year ago?

-   BUS12: Does the respondent think that during the next 12 months we'll have good times financially, or bad times, or what?

-   HOM: Home buying attitudes.

-   HOMEVAL: Does the respondent think the value of their home is higher or lower compared to a year ago?

-   INVEST: Does the respondent have stocks?

-   INVAMT: How much are the respondents’ total investments worth today?

-   PSTK: What does the respondent think is the percent chance that a one thousand dollar investment in a diversified stock mutual fund will increase in value in the year ahead, so that it is worth more than one thousand dollars one year from now?

-   POLAFF: Does the respondent consider themself a Democrat, Republican, or Independent?

-   GASPX1: Does the resondent think that the price of gasoline will go up during the next five years, will gasoline prices go down, or will they stay about the same as they are now?

-   HOMEAMT: Market value of respondents’ home in the given year

-   HOMEOWN: Does the respondent own their own home, pay rent, or something else?




Please see our EDA page for more information on these variables and their relationship with INCOME. We use the same independent variables in each of our models for comparison purposes.

"""

text_chunk5 = """

#### Train/Test Split


"""

text_chunk6 = """


#### Summaries of Each Model



##### Linear Regression

Linear regression is a statistical model that aims to establish a linear relationship between a dependent variable (in this case, income) and one or more independent variables (we use all the social variables listed above). The model assumes that the relationship between the variables is linear and uses the coefficients of the independent variables to predict the value of the dependent variable. 



Our linear model performed with an MSE of XXXXXXX and an R-squared of XXXXXXXX. OTHER NOTES ON LINEAR REGRESSION.

INSERT OUTPUT???

##### Lasso Regression

Lasso regressions are a subset of linear regression that are used for feature selection and regularization. With so many categories in our categorical variables, we ended up with more than 50 variables in our linear regression. With this, the lasso regression could help shrink the coefficients of some of the less important independent variables to zero. This allows for a simpler model that includes only the most important independent variables, which can help to reduce overfitting and improve prediction accuracy.



Our linear model performed with an MSE of XXXXXXX and an R-squared of XXXXXXXX. OTHER NOTES ON LASSO REGRESSION.



INSERT OUTPUT???



##### Elastic Net

Elastic net is a hybrid of the lasso and ridge regressions. It can help prevent overfitting, help with feature selection, and regularization. It combines the L1 penalty of the lasso regression with the L2 penalty of the ridge regression.



Our elastic net performed with an MSE of XXXXXXX and an R-squared of XXXXXXXX. OTHER NOTES ON ELASTIC NET.



INSERT OUTPUT???



##### Generalized Additive Models (GAM)

GAM is a subset of the regression model that allows for nonlinear relationships between the dependent variable (in our case, income) and our societal independent variables. It does this by adding a smoothing function to the independent variables instead of assuming linearity in the relationships. This could be an improvement over our linear regression because it can model the complex, possibly non-linear relationships between social determinants and income that a linear model cannot capture.



Our GAM performed with an MSE of XXXXXXX and an R-squared of XXXXXXXX. OTHER NOTES ON GAM.



INSERT OUTPUT???



##### XG Boost

XG Boost is a machine learning algorithm that can be used in place or a regression. It combines a lot of weak decision trees to form a stronger predictive model. XG Boost is good at handling large datasets with many features like the one we have, and it can achieve a strong prediction accuracy in classification tasks. Like the Lasso Regression and Elastic Net, it can also be used for identifying the most important features in predicting income.



Our XG Boost performed with an MSE of XXXXXXX and an R-squared of XXXXXXXX. OTHER NOTES ON XG Boost.



INSERT OUTPUT???
"""

layouts = [
    html.Br(), html.Div(dcc.Markdown(text_chunk1), style=div_style),
    html.Br(), html.Div(dcc.Markdown(text_chunk2), style=div_style),
    html.Br(), html.Div(dcc.Markdown(text_chunk3), style=div_style),
    html.Br(), html.Div(dcc.Markdown(text_chunk4), style=div_style),
    html.Br(), html.Div(dcc.Markdown(text_chunk5), style=div_style),
    html.Br(), html.Div(dcc.Markdown(text_chunk6), style=div_style)
]


models_layout = html.Div(layouts)
