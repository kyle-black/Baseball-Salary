# Where do wins come from? 
## Using Machine Learning to find optimal Run differentials. 

<p> Baseball's Sabermetric pioneer Bill James created the Pythageron Win Expectation Ratio to estimate the amount of wins a team could expect based on the  amount ratio of runs scored to runs allowed. <br>
$$W_{expected wins} = \frac{runs scored^2}{runs scored^2 + runs allowed ^2} \frac**

This was later revised to as 1.83 was a better fit for the regression line:
$$W_{expected wins} = \frac{runs scored^1.83}{runs scored^1.83 + runs allowed ^1.83} \frac </p>



Using Run Differential data (Runs scored - Runs Allowed) from the 2011 to 2022 seasons (excluding 2020 covid season). I've recalculated the regression line of wins to Run Difference using gradient decent. 

$$ y= mx+c $$







