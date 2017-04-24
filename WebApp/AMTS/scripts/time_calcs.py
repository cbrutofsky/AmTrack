from datetime import *
from geopy.distance import vincenty
import math


def distance_traveled(range_data):
    distance = 0
    for item in range(0, len(range_data)-1):
        location1 = (range_data[item].latitude, range_data[item].longitude)
        location2 = (range_data[item+1].latitude, range_data[item+1].longitude)
        temp_dist = dist_between_two(location1, location2)
        distance += temp_dist
    distance = round(distance, 4)
    return distance  # miles


def dist_between_two(location1, location2):
    temp = (location1[0], location1[1])
    temp2 = (location2[0], location2[1])
    distance = vincenty(temp, temp2).miles
    return distance


def get_total_time(start_date, end_date):
    time_diff = end_date - start_date
    days = time_diff.days
    hours = round(time_diff.seconds/3600, 4)
    total_time = [days, hours]
    return total_time


def get_time_on(range_data):
    time_on = timedelta(0, 0, 0)
    for item in range(0, len(range_data)-1):
        diff = time_between_two(range_data[item].CollectionTime, range_data[item+1].CollectionTime)
        if diff.seconds/60 < 10:
            time_on += diff
    days = time_on.days
    hours = round(time_on.seconds/3600, 4)
    time_on_f = [days, hours]
    return time_on_f


def time_between_two(time1, time2):
    diff = time2 - time1
    return diff


def get_time_idle(range_data):
    time_idle = timedelta(0, 0, 0)
    for item in range(0, len(range_data) - 1):
        diff = time_between_two(range_data[item].CollectionTime, range_data[item + 1].CollectionTime)
        if diff.seconds / 60 < 10:
            time_idle += diff
    days = time_idle.days
    hours = round(time_idle.seconds / 3600, 4)
    time_idle_f = [days, hours]
    return time_idle_f


def get_time_off(time_on, total_time):
    total_time_comp = timedelta(total_time[0], total_time[1])
    time_on_comp = timedelta(time_on[0], time_on[1])
    diff = total_time_comp - time_on_comp
    days = diff.days
    hours = round(diff.seconds/3600, 4)
    time_off = [days, hours]
    return time_off


def get_average_speed(range_data):
    total_speed = 0.0
    count = len(range_data)
    for item in range_data:
        if not math.isnan(float(item.speed)):
            total_speed += float(item.speed)
    try:
        avg_speed = total_speed/count
    except ZeroDivisionError:
        avg_speed = 0
    avg_speed_mph = avg_speed * 2.23694
    avg_speed_mph = round(avg_speed_mph, 4)
    return avg_speed_mph