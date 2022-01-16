# Introduction 

We have access to 285,000 Yelp reviews of restaurants in the Phoenix area. From the dataframe, we can see that each review contains features of three main categories:
1) Business features: For each business, we know the basic features including locations, operation hours, stars, price range, review count, etc.
2) User features: For each user, we know the user's reviews, the user's review counts, and the user's account information, as well as past behavioral data.
3) Review features: For each review, we know information such as its ID, which restaurant it is written for, and how many times it has been voted as useful/cool/funny, etc.

## Yelp Business Goal:
- businesses: uses Yelp as a platform for more exposure and more customers. Yelp has been recognized as a verified and accountable entity in which people can place their trust and access good local businesses.
- users: forms a vibrant community of active reviewers that are engaged in fun social exchanges

### In the following analysis, we seek to answer these questions:
1) How many businesses are there and what does the distribution of their average ratings look like?
2) Is business average rating related to other attributes such as categories, price range, and review counts?
3) Is there any difference between the geographic locations of businesses with higher average ratings and those with lower ratings?
4) Does there exist toxic commentator who tend to give lower ratings for all businesses? If so, how can Yelp identify these users?
5) What factors impact a review's rating? Can we accurately predict a review's rating based on these factors?
To answer these questions, I will split the analysis into three sections. The first section looks at all unique businesses and identify relationships between certain business attributes and their average ratings. The second section examines all the reviews and investigate the influence of various factors on review ratings. Finally, the last section would look at all the users and try to identify the characteristics of toxic commentators.
