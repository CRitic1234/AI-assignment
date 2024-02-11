def date_decoder (date):
    month_name=["january", "february", "march", "april", "may", "june","july","august","september","october","november","december"]
    month_num=[1,2,3,4,5,6,7,8,9,10,11,12]
    month_dict={x:y for x,y in zip(month_name,month_num)}  #zip() func to patch two lists into a dictionary
    # print("Month Name and Month Number Dictionary:\n",month_dict)

    day,month,year=date.split(sep='-')
    # print(f"day={day},month={month},year={year}")

    month=month_dict[month]
    # print(month)

    integer_year=int(year)   #type casting string to integer
    integer_day=int(day)

    #correcting the year
    if integer_year>24:
        integer_year=1900+integer_year
    else:
        integer_year=2000+integer_year

    date_decoded=(integer_day,month,integer_year)
    return date_decoded



#taking string input
date=str(input("enter the date in format dd-month_name-year:"))
# date="8-march-85"
print(date_decoder(date))






