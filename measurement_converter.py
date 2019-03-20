#Measurement converter

meter = float(input('Distance in meter:'))

km = meter / 1000
cm = meter * 100
mm = meter * 1000

print('The distance of {} in meters, correspond:\
    {}km\n \
    {}cm\n\
    {}mm'.format(meter, km, cm, mm))