Chapter 10 Assignment

def get_country_codes(prices):

    i = 0
    new_prices = prices.split(",")
    for var in new_prices:
        indexDollar = var.index("$")
        countryCode = var[:indexDollar]   #take the countryCode
        new_prices[i] = countryCode
        i = i + 1		                  #increment list

    return ",".join(new_prices)


print(get_country_codes("AU$104, US$34"))

#[AU, US]

#"AU, US"

#Takeaways: join automatically puts spaces between list items between your delimiter.
#you can split a string and bring it back together with the join method
