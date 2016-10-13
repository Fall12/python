import os, json, sys
import time


# Handle file and json.
# change time by seconds to 2016-10-12 17:45:00.
if __name__ == '__main__':
    soure_file = open('soure.log', 'r')
    log_file = open('log.log', 'a+')
    for line in soure_file:
        # 指定分隔符
        line = line.strip()
        try:
            logdata = json.loads(line)
            x = time.localtime(int(logdata['time'] / 1000))
            dataArry = time.strftime("%Y-%m-%d %H:%M:%S", x)
            newdata = {
                'test': logdata['test'],
                'time': dataArry,
            }
            
            jsonData = json.dumps(newdata, ensure_ascii=False)
            # Write to file.
            log_file.write(jsonData)
        except BaseException as e:
            print('Error: ', e)
            break
    log_file.close()
    soure_file.close()
    print('stop')
