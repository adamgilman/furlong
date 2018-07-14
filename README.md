# Hello Furlong
Furlong aims to make units conversions easy and pythonic with a simple to understand and magical interface. Simply declare the unit and value and convert to anything you can think of. If we don't support a unit conversion, open a pull request to add it for everyone!

## How it works
Bring Furlong into your project with a simple name, f is recommended but, not required

`from furlong import Furlong as f`

Declare the unit and value of the base measurement

`length_of_wall = f(inches=300)`

Then convert to any unit you'd like!

```
length_of_wall.asCentimeters()
30.48
```

Done!

## Error handling

* [TODO]

## Units supported

* ### Length
    * inches
    * centimeters

* ### Volume

* ### Weight
