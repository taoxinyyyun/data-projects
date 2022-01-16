library(quantmod);library(tseries);
library(timeSeries);library(forecast);library(xts);


# loading daily stock price data csv
INTC_STOCKPRICE = read.csv('/Users/sallyxinyueyu/downloads/INTC.csv')
str(INTC_STOCKPRICE)
View(INTC_STOCKPRICE)
length(INTC_STOCKPRICE$Date)
length(INTC_STOCKPRICE$Adj.Close)
## plot the adjusted stock price
library(ggplot2)
qplot(Date, Adj.Close,data = INTC_STOCKPRICE)


# Create data frame with date and adj.close price 
adj_closing_prices  <- INTC_STOCKPRICE[, "Adj.Close", drop = F]
head(adj_closing_prices)
## Create a new data frame that contains the price data with the dates as the row names
INTC_STOCKPRICE_prices <- INTC_STOCKPRICE[, "Adj.Close", drop = FALSE]
rownames(INTC_STOCKPRICE_prices) <- INTC_STOCKPRICE$Date
head(INTC_STOCKPRICE_prices)
tail(INTC_STOCKPRICE_prices)
## Plotting the adj.close price with timeseries
plot(INTC_STOCKPRICE_prices$Adj.Close, type="l", col="blue", lwd=2, 
     ylab="Adjusted closing Price", main="Adj.Closing price of INTC")



# Caculating the simple Return 

## Denote n the number of time periods:
n <- nrow(INTC_STOCKPRICE_prices)
INTC_STOCKPRICE_return <- ((INTC_STOCKPRICE_prices[2:n, 1] - INTC_STOCKPRICE_prices[1:(n-1), 1])/INTC_STOCKPRICE_prices[1:(n-1), 1])
# Now add dates as names to the vector 
names(INTC_STOCKPRICE_return) <- INTC_STOCKPRICE[2:n, 1]
head(INTC_STOCKPRICE_return)
# Plot the simple returns of INTC
plot(INTC_STOCKPRICE_return, type = "l", col = "blue", lwd = 2, ylab = "Simple Return",
     main = "Daily Returns on INTC")

# Analyzing the adj.close and simple return 
library(psych) 
describe(INTC_STOCKPRICE$Adj.Close)
describe(INTC_STOCKPRICE_return)
hist(INTC_STOCKPRICE_return, nclass = 200)

# ACF and PACF Criterion for Adj.close price
install.packages("fBasics")
library(fBasics)
acf(INTC_STOCKPRICE$Adj.Close, lag.max = 50, plot = TRUE)
pacf(INTC_STOCKPRICE$Adj.Close, lag.max = 50, plot = TRUE)

timeseries <- ts(INTC_STOCKPRICE$Adj.Close, frequency = 12)
timeseriescomponents <- decompose(timeseries)
plot(timeseriescomponents)
################################################################################


# Computing the log returns for the INCT
log_data = log(INTC_STOCKPRICE$Adj.Close)
log_ret = diff(log_data, differences = 1)
#Data Cleaning
na.omit(log_ret)
INTC_log_ret <- na.omit(log_ret)
# Plot log returns 
plot(INTC_log_ret,type='l', main='log returns plot')
print(adf.test(INTC_log_ret))

# Determine the Order in ARIMA model
pacf(INTC_log_ret, lag.max = 20, main = "PACF on INTC_Log Return")
acf(INTC_log_ret, lag.max = 20, main = "ACF on INTC_Log Return")

# Conduct ADF test on log returns series
print(adf.test(INTC_log_ret))
count_d1 = diff(INTC_STOCKPRICE$Adj.Close, differences = 1)
plot(count_d1)

ndiffs(log_ret)
hist(log_ret, nclass = 200)
# Split the dataset in two parts - training and testing
INTC_log_ret_train = INTC_log_ret[1:3000]
length(INTC_log_ret_train)
INTC_log_ret_test = INTC_log_ret[3001:3525]
length(INTC_log_ret_test)

# AR1 Model1
# (Summary of the ARIMA model using the determined (p,d,q) parameters)
model1 = arima(INTC_log_ret_train, order = c(1, 1, 0),include.mean=FALSE)
summary(model1)
tsdisplay(model1$residuals)


#AR1 Model2 
# (graph shows serious lag at 15, so modify model for p or q = 15)
model2 = arima(INTC_log_ret_train, order = c(15, 1, 1),include.mean=FALSE)
summary(model2)
tsdisplay(model2$residuals, lag.max = 30)
# forcast new arima model for h = 30 period (30 days)
model_forecast = forecast(model2,h = 1,level=99)
model_forecast
head(model_forecast)
install.packages("lmtest")
library(lmtest)
dwtest(model_forecast)
Box.test(model2$residuals, lag = 2, type = 'Ljung-Box')

# Creating a series of forecasted returns for the forecasted period
forecasted_series = rbind(forecasted_series,arima.forecast$mean[1])
colnames(forecasted_series) = c("Forecasted")
# Creating a series of actual returns for the forecasted period
Actual_return = stock[(b+1),]
Actual_series = c(Actual_series,xts(Actual_return))
rm(Actual_return)

print(stock_prices[(b+1),])
print(stock_prices[(b+2),])

# Adjust the length of the Actual return series
Actual_series = INTC_STOCKPRICE[-1]
# Create a time series object of the forecasted series
forecasted_series = xts(forecasted_series,index(Actual_series))
# Create a plot of the two return series - Actual versus Forecasted
plot(Actual_series,type='l',main='Actual Returns Vs Forecasted Returns')
lines(forecasted_series,lwd=1.5,col='red')
legend('bottomright',c("Actual","Forecasted"),lty=c(1,1),lwd=c(1.5,1.5),col=c('black','red'))
# Create a table for the accuracy of the forecast
comparsion = merge(Actual_series,forecasted_series)
comparsion$Accuracy = sign(comparsion$Actual_series)==sign(comparsion$Forecasted)
print(comparsion)
# Compute the accuracy percentage metric
Accuracy_percentage = sum(comparsion$Accuracy == 1)*100/length(comparsion$Accuracy)
print(Accuracy_percentage)



accuracy(model2,x = INTC_log_ret_test)
plot(model2$residuals, model_forecast[-1])
return_forecast= ts(model_forecast)
return_forecast
library(ggplot2)

install.packages("fGarch")
library(fGarch)

install.packages("aTSA")
library(aTSA)
arch.test(model2, output = TRUE)
