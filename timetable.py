import pandas as pd


def get_core_time_table(section, day):
    data = pd.read_csv('sem-6-time-table.csv')
    # filter_by_section = data.groupby('Section')
    # sec_group = filter_by_section.get_group(section)

    sec_group = filter_by_section(data, section)

    base = sec_group.index[0]

    day_index = {
        'MON': base + 0,
        'TUE': base + 1,
        'WED': base + 2,
        'THU': base + 3,
        'FRI': base + 4,
    }

    return {
        'DAY': sec_group['DAY'][day_index.get(day)],
        'ROOM1': sec_group['ROOM1'][day_index.get(day)],
        '8-9': sec_group['8-9'][day_index.get(day)],
        '9-10': sec_group['9-10'][day_index.get(day)],
        '10-11': sec_group['10-11'][day_index.get(day)],
        'ROOM2': sec_group['ROOM2'][day_index.get(day)],
        '11-12': sec_group['11-12'][day_index.get(day)],
        '12-1': sec_group['12-1'][day_index.get(day)],
        '1-2': sec_group['1-2'][day_index.get(day)]
    }


def get_ele_time_table(section, day):
    data = pd.read_csv('sem-6-elective-time-table.csv')
    # filter_by_section = data.groupby('Section')
    # sec_group = filter_by_section.get_group(section)

    sec_group = filter_by_section(data, section)

    base = sec_group.index[0]

    day_index = {
        'MON': base + 0,
        'TUE': base + 1,
        'WED': base + 2,
        'THU': base + 3,
        'FRI': base + 4,
    }

    return {
        'DAY': sec_group['DAY'][day_index.get(day)],
        'ROOM1': sec_group['ROOM1'][day_index.get(day)],
        '11-12': sec_group['11-12'][day_index.get(day)],
        'ROOM2': sec_group['ROOM2'][day_index.get(day)],
        '12-1': sec_group['12-1'][day_index.get(day)],
        'ROOM3': sec_group['ROOM3'][day_index.get(day)],
        '1-2': sec_group['1-2'][day_index.get(day)],
        'ROOM4': sec_group['ROOM4'][day_index.get(day)],
        '3-4': sec_group['3-4'][day_index.get(day)],
        'ROOM5': sec_group['ROOM5'][day_index.get(day)],
        '4-5': sec_group['4-5'][day_index.get(day)]
    }


def filter_by_section(data, section):
    return data.groupby('Section').get_group(section)
