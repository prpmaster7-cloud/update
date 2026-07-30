import uuid
import random


def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'):  return '2009'
        if uid.startswith('10000000'):   return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid.startswith('100001'):  return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'):  return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
        if uid.startswith('100009'):  return '2015'
        if uid.startswith('10001'):   return '2016'
        if uid.startswith('10002'):   return '2017'
        if uid.startswith('10003'):   return '2018'
        if uid.startswith('10004'):   return '2019'
        if uid.startswith('10005'):   return '2020'
        if uid.startswith('10006'):   return '2021'
        if uid.startswith('10009'):   return '2023'
        if uid.startswith(('10007', '10008')): return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8:       return '2007'
    elif len(uid) == 7:       return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    return ''


def fake_device_ids():
    return {
        'adid':             str(uuid.uuid4()),
        'device_id':        str(uuid.uuid4()),
        'family_device_id': str(uuid.uuid4()),
        'advertiser_id':    str(uuid.uuid4()),
    }


def gen_uid_all_series(limit, range_choice='1'):
    uids = []
    star = '10000'
    for _ in range(limit):
        n = random.choice(range(1000000000, 1999999999 if range_choice == '1' else 4999999999))
        uids.append(star + str(n))
    return uids


def gen_uid_100003_100004(limit):
    uids = []
    for _ in range(limit):
        prefix = random.choice(['100003', '100004'])
        uids.append(prefix + ''.join(random.choices('0123456789', k=9)))
    return uids


def gen_uid_2009(limit):
    uids = []
    for _ in range(limit):
        uids.append('1000004' + ''.join(random.choices('0123456789', k=8)))
    return uids
