def build_car(manufacturer, model, **addition):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in addition.items():
        car[key] = value
    return car

x = 0.1 + 0.1 + 0.1 + 0.1 + 0.1
if 0.5 == x:
    print ('rrrr')
print (x)