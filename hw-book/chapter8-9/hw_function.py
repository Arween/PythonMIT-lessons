def build_car(manufacturer, model, **addition):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in addition.items():
        car[key] = value
    return car

