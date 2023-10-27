# zip function with two dict

country=['India','Australia','United states','England']
city=['New Delhi','Camberra','Washington DC','London'] 

country_city = list(zip(country,city))                          # to return in list
print(country_city)
Output:
[('India', 'New Delhi'),
 ('Australia', 'Camberra'),
 ('United states', 'Washington DC'),
 ('England', 'London')]

country_city = dict(zip(country,city))                        # to return in dictionary
print(country_city)
Output:
        {('India', 'New Delhi'),
         ('Australia', 'Camberra'),
         ('United states', 'Washington DC'),
         ('England', 'London')}
