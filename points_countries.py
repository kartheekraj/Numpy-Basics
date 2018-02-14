import numpy as np
from pandas import DataFrame, Series

'''Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each 
    bronze medal.  

    Using the numpy.dot function, create a new dataframe called 
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.
           
    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

#Combining the lists:
OMC={'Country':Series(countries),'gold':Series(gold),'silver':Series(silver),'bronze':Series(bronze)}

#Converting the list into a DataFrame:
OMC_df= DataFrame(OMC)

'''Creating olympic points each gold is worth 4 points and silver and bronze are 2,1 respectivly'''
medal_count=OMC_df[['gold','silver','bronze']]
points = np.dot(medal_count,[4,2,1])

#Creating a new DataFrame with countries name corresponding their points:
olympic_points = DataFrame({'Country':Series(countries),'points':Series(points)})
print(olympic_points)
