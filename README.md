# Ukranian TSP Project
Project started as a part of an Artificial Intelligence course. Uses TSP to calculate the shortest route possible through Ukraine's 50 largest cities using Google Maps API data!

# How to use

Running the file as-is gets you the shortest path to visit cities when we consider Euclidean distance between the cities, a starting point of Kyiv, and only one car running at a time. 

## Using the Google Maps distance API and starting at Przemysl, Poland, this is the best path:

Przemysl -> Uzhhorod -> Mukacheve -> Ivano-Frankivsk -> Chernivtsi -> Kamianets-Podilskyi -> Khmelnytskyi -> Vinnytsia -> Uman -> Kropyvnytskyi -> Kherson -> Yevpatoriia -> Sevastopol -> Simferopol -> Melitopol -> Berdiansk -> Mariupol -> Donetsk -> Makiivka -> Horlivka -> Khrustalnyi -> Dovzhansk -> Luhansk -> Alchevsk -> Lysychansk -> Sievierodonetsk -> Kramatorsk -> Sloviansk -> Kharkiv -> Poltava -> Kremenchuk -> Kamianske -> Dnipro -> Pavlohrad -> Zaporizhzhia -> Nikopol -> Kryvyi Rih -> Mykolaiv -> Odesa -> Cherkasy -> Sumy -> Konotop -> Chernihiv -> Brovary -> Kyiv -> Bila Tserkva -> Zhytomyr -> Rivne -> Lutsk -> Ternopil -> Lviv -> Drohobych -> Przemysl

## On a map, the API path looks like this:  
[<img width="818" alt="image" src="https://media.github.umn.edu/user/18632/files/8b05f2e7-3d39-4000-ba5b-68d578d2e45e">](https://www.google.com/maps/d/u/0/edit?mid=105ki4-FEWln_pj7D4b2LH-XD1BV_bNoW&usp=sharing)

Przemysl, PL is highlighted with the orange star pin.



## Using Euclidean distance, this is the best path:    
  
Kyiv -> Brovary -> Chernihiv -> Konotop -> Sumy -> Kharkiv -> Poltava -> Kremenchuk -> Kryvyi Rih -> Nikopol -> Zaporizhzhia -> Kamianske -> Dnipro -> Pavlohrad -> Kramatorsk -> Sloviansk -> Lysychansk -> Sievierodonetsk -> Alchevsk -> Luhansk -> Dovzhansk -> Khrustalnyi -> Horlivka -> Makiivka -> Donetsk -> Mariupol -> Berdiansk -> Melitopol -> Simferopol -> Sevastopol -> Yevpatoriia -> Kherson -> Mykolaiv -> Odesa -> Kropyvnytskyi -> Cherkasy -> Bila Tserkva -> Vinnytsia -> Khmelnytskyi -> Kamianets-Podilskyi -> Chernivtsi -> Ivano-Frankivsk -> Mukacheve -> Uzhhorod -> Drohobych -> Lviv -> Ternopil -> Lutsk -> Rivne -> Zhytomyr -> Kyiv  
  
## On a map, the Euclidean path looks like this:  
[<img width="807" alt="image" src="https://media.github.umn.edu/user/18632/files/17b21629-72d5-4c82-8f0f-e2d54980d744">](https://www.google.com/maps/d/u/0/edit?mid=1GUJCu9g-rWXBjZ3zbNBrBHiP08vjkPJi&usp=sharing)
  
Kyiv is highlighted with the orange star pin.

# Areas for Improvement
Potential changes to include:  
- have the start node be somewhere in a surrounding city from a different country instead of Kyiv  
- explore the effect of having multiple cars
- be able to update with real-time war-zone data

# Resources
- [Google OR Tools](https://developers.google.com/optimization/routing/tsp#python_14) authored the codebase I modified for this problem
- [This website](https://www.movable-type.co.uk/scripts/latlong.html) has the algorithm I used to calculate Euclidean distance between coordinates in JavaScript code.
- [This google map](https://www.google.com/maps/d/u/0/edit?mid=1GUJCu9g-rWXBjZ3zbNBrBHiP08vjkPJi&usp=sharing), which I've used to illustrate the path
- [This google sheet](https://docs.google.com/spreadsheets/d/1wxR2lCaWynAaf1AM-dx1Ek2kexnu9nbs7rZZ06kpK4Q/edit?usp=sharing) detailing 1469 Ukranian cities, along with their population and coordinates. The original database [can be found here](https://simplemaps.com/data/ua-cities).


