CalCalc
=======

Calorie Calculator

This is my first Github project. The idea was to get familiar with the github interface and develop a little calorie
calculator Python script.

A calorie calculator tells you how many calories and the protein/carbs/fats distribution that you should eat in a meal
according to your needs. It is a very powerful tool to get the body you want. This project was inspired by the "You are
your own gym" book by Mark Lauren that I recommend to everyone.

This script has six inputs:
  1. Gender: "male" or "female".
  2. Weight: Your actual weight in kg.
  3. Height: Your actual height in cm.
  4. Age: Your age.
  5. Activity: The amount of activity you do:
    0. Sedentary: "0"
    1. 1-3 days/week: "1"
    2. 3-5 days/week: "2"
    3. 6-7 days/week: "3"
    4. Professional athlete: "4"
  6. Goal: Your goal:
    0. Loose weight: "0"
    1. Maintain weight: "1"
    2. Gain weight: "2"
    
So if you are 22 years old male that weights 81kg and a height of 178cm, and your objective is to loose weight by doing exercise 1-3 days per week, you would type in the console: 

```
python CalCalc.py male 80 178 22 2 0
```
And the output would be:
```
(2448, 34, 52, 15)
```
The first element is the calories per day followed by the carbs/proteins/fats per meal that you should eat.

I hope you find this a useful tool. I am Ricardo Garzo Castro, Electronics Engineer. Feel free to contact me at ricardogarzocastro@gmail.com. 
