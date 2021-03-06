import json
import sys
import datetime as dt
import re


def epicenter_record_to_dic(line: str):
    year = int(line[1:5])
    month = int(line[5:7])
    day = int(line[7:9])
    hour = int(line[9:11])
    minute = int(line[11:13])
    second_str = line[13:15]
    second = 0
    if(second_str == '  '):
        second_str = 0
    else:
        second = int(second_str)

    latitude_degree = line[21:24]
    latitude_minute = line[24:28]

    longitude_degree = line[32:36]
    longitude_minute = line[36:40]

    dic = {}
    small_area_class_num_str = line[65:68]
    if small_area_class_num_str == '   ':
        dic["small_area_class_num"] = 0
    else:
        dic["small_area_class_num"] = int(small_area_class_num_str)
    dic["observ_point_num"] = int(line[-6:-1])

    dic["latitude"] = int(latitude_degree) + (int(latitude_minute[:2]) / 60)
    dic["longitude"] = int(longitude_degree) + (int(longitude_minute[:2]) / 60)

    dic["time"] = str(dt.datetime(year, month, day, hour=hour,
                                  minute=minute, second=second))

    return dic


def open_code_p():
    code_p = {}
    with open('record/code_p') as f:
        line = f.readline().replace('\n', '')
        while line:
            line_splited = line.split()
            latitude_minute = int(line_splited[2][2:])
            longitude_minute = int(line_splited[3][3:])
            code_p[line_splited[0]] = {}
            code_p[line_splited[0]]["latitude"] = int(
                line_splited[2][:2]) + (latitude_minute / 60)
            code_p[line_splited[0]]["longitude"] = int(
                line_splited[3][:3]) + (longitude_minute / 60)

            line = f.readline().replace('\n', '')

    return code_p


def intensity_record_to_dic(line: str):
    dic = {}
    dic["observ_point_num"] = line[0:7]
    dic["intensity"] = line[18]

    return dic


def intensities_add_record(intensities: list, line: str):
    intensities.append(intensity_record_to_dic(line))
    if intensities[-1]["observ_point_num"] not in code_p:
        del intensities[-1]
    else:
        intensities[-1]["latitude"] = code_p[intensities[-1]
                                             ["observ_point_num"]]["latitude"]
        intensities[-1]["longitude"] = code_p[intensities[-1]
                                              ["observ_point_num"]]["longitude"]


if __name__ == '__main__':

    MIN_INTENSITY = '2'  # 1-7で
    if len(sys.argv) <= 2:
        print('引数を指定して')
        sys.exit()

    json_dic = {"data": []}
    record_path = sys.argv[1]
    save_filename = sys.argv[2]

    code_p = open_code_p()

    with open(record_path) as f:
        # record_lines = [s.replace('\n', '') for s in f.readlines()]

        line = f.readline().replace('\n', '')
        while line:
            if re.match(r'^A.{60}[' + MIN_INTENSITY + r'-7A-D]', line):
                # print(line)
                json_dic["data"].append(epicenter_record_to_dic(line))
                json_dic["data"][-1]["intensities"] = []
                intensities = json_dic["data"][-1]["intensities"]

                for i in range(json_dic["data"][-1]["observ_point_num"]):
                    line = f.readline().replace('\n', '')
                    # print(line)

                    intensities_add_record(intensities, line)

            elif re.match(r'^B.{60}[' + MIN_INTENSITY + r'2-7A-D]', line):
                # print(line)
                json_dic["data"].append(epicenter_record_to_dic(line))
                json_dic["data"][-1]["intensities"] = []
                intensities = json_dic["data"][-1]["intensities"]

                for i in range(json_dic["data"][-1]["observ_point_num"]):
                    while re.match(r'^B', line := f.readline().replace('\n', '')):
                        continue
                    # print(line)
                    intensities_add_record(intensities, line)

            line = f.readline().replace('\n', '')

        with open('record/' + sys.argv[2], 'w') as f:
            json.dump(json_dic, f, indent=4)
