# Polygon

Using Polygon.io’s API, you’ll be pulling down data, cleaning the data, storing the data in a database, and then querying the data and performing calculations that will also be added to the database. After the calculations are done, you’ll be doing work to visualize the data as well.


Step 1:

Build automated 1second, 1 minute, and daily bar data collection each day for all symbols for that specific day’s symbol universe.

Skills you’ll practice:
    ⁃    Automation
    ⁃    working with APIs.
    ⁃    Database management
    ⁃    Data cleansing

Using polygon’s REST API, I want you to create a program that collects every 1 second, 1 minute, and daily bar data available on polygon for every stock on each day.

In order to do this, you’ll first need to get a list of every ticker symbol that is available on a given day. Polygon’s API has a function for this where you feed it a date and it gives you a list for that day. If you look at their documentation or ask something like chatgpt it will show you how. It’s important that you use this because stocks come and go over time. So for any historical day, there can be new stocks compared to another day.

So, collect the data for the bars I mentioned before going all the way back to 2018-01-01 (can go back to 2004 if it’s not enough data for you).

For cleansing the data, you can start off with simple checks like seeing if there are negative numbers for datapoints that should not have a negative number (like the price or volume). If you think of any other ones that you think are relevant lmk and we can discuss them. I want you to save the data in an organized way as CSVs as well as saving the data in a local database so you can practice your sql skills.

If you’re feeling it, you can practice your automation skills and make a program that runs every night at like 2am that pulls the previous day’s data and saves these CSVs and also enters data into the database. This is what you’d need to do for building out a cloud pipeline.




Step 2:
You’re going to query the data from your database to create two “summary” sheets for every single stock for every single day. So basically, a stock (let’s use “AAPL”) should have two unique summary sheet for EACH date in your database. The reason for having two is because one summary sheet will be made for features/datapoints that are known coming into the day (let’s call it “beginning of day” or “BOD” sheet) and the other is like an “after the fact” summary sheet for when the day is over (let’s call that one “end of day” or “EOD”).


Skills you’ll practice:
    ⁃    database querying
    ⁃    Analysis and interpretation
    ⁃    Data cleansing
    ⁃    Automation


Each summary sheet will include a whole bunch of data. The reason we want this data is because we can use these datapoints to create filters when querying for specific stocks for a specific day (which we’ll use in step 3 when we do the deeper analysis).


Datapoints in the BOD summary:
    ⁃    yesterday’s open px (px = price)
    ⁃    yesterday’s high px
    ⁃    yesterday’s low px
    ⁃    yesterday’s close px
    ⁃    yesterday’s volume traded
    ⁃    21 day ATR (average true range, can find calculation online)
    ⁃    21 day average volume
    ⁃    Last “X” day’s maximum high (replace X with 2,3,4,5,10,15,30,60,90,180,360)
    ⁃    Last “X” day’s minimum low (replace X with 2,3,4,5,10,15,30,60,90,180,360)
    ⁃    Last “X” day’s range [max high - min low] (replace X with 2,3,4,5,10,15,30,60,90,180,360)
    ⁃    Last “X” day’s range as a pct [(max high - min low) / min low] (replace X with 2,3,4,5,10,15,30,60,90,180,360)
    ⁃    “X” day’s simple moving average [calculations available online] (replace X with 5,10,20,30,50,100,200)
    ⁃    “X” day’s exponential moving average [calculations available online] (replace X with 5,10,20,30,50,100,200)



EOD summary features (replace “yesterday’s” with today, sorry I’m typing on phone)

    ⁃    Yesterday’s range (yesterday high - low)
    ⁃    Yesterday’s range as a pct ((yesterday high - low)/ yesterday low)
    ⁃    Yesterday’s premarket high price (query minute bars from yesterday that correspond to the premarket trading hours [times before 9:30am EST] and find the maximum high.
    ⁃    Yesterday’s premarket low price (query minute bars from yesterday that correspond to the premarket trading hours [times before 9:30am EST] and find the minimum low.




Step 3:
Visualizing the data. Let’s cross this bridge when we get there because I think by the time we’re here, the needs might look a little different.



## Remember, their github has efficient code for what I need to do. No need to reinvent the wheel
