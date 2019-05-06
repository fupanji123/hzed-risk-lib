import logging
from logging.handlers import TimedRotatingFileHandler
import os
import re
import requests
import json

#创建logger
def create_logger(LOG_PATH, level=logging.INFO, record_format=None):
    """Create a logger according to the given settings"""
    if record_format is None:
        record_format = "%(asctime)s\t%(levelname)s\t%(module)s.%(funcName)s\t%(threadName)s\t%(message)s"

    logger = logging.getLogger("parseLogger")
    logger.setLevel(level)

    # 日志滚动输出
    if not logger.handlers:
        fh = TimedRotatingFileHandler(filename=LOG_PATH + r"\\parseLogger.log", when="D", interval=1, backupCount=60)
        fh.suffix = "%Y-%m-%d_%H-%M.log"
        fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")

        # 简单文件输出
        # fh = logging.FileHandler(LOG_PATH + 'sys.log')
        fh.setLevel(level)

        # 控制台输出
        ch = logging.StreamHandler()
        ch.setLevel(level)

        formatter = logging.Formatter(record_format)

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger

def getjson(url):
    try:
        req = requests.get(url,timeout=15)  # 请求链接，15秒无响应则抛出异常
    except:
        try:
            req = requests.get(+url,timeout=15) # 请求链接，15秒无响应则抛出异常
        except:
            return '请求超时'
    return req


data_1 = {'tz-feature38': '','tz-feature34': '','tz-feature35': '','tz-feature36': '','tz-feature37': '','tm-feature52': '','sv4-feature19': '','tm-feature51': '','tm-feature50': '','sv4-feature17': '',
              'sv4-feature18': '','sv4-feature22': '','ct-feature13': '','tm-feature49': '','sv4-feature23': '','ct-feature14': '','tm-feature48': '','sv4-feature20': '','ct-feature15': '','tm-feature47': '',
              'sv4-feature21': '','ct-feature16': '','tm-feature46': '','sv4-feature26': '','tm-feature45': '','sv4-feature27': '','ct-feature10': '','tm-feature44': '','sv4-feature24': '','ct-feature11': '',
              'tm-feature43': '','sv4-feature25': '','ct-feature12': '','tm-feature42': '','tz-feature30': '','tz-feature31': '','tz-feature32': '','tz-feature33': '','ti-feature2': '','ti-feature3': '','ti-feature4': '',
              'ti-feature5': '','ti-feature1': '','tm-feature41': '','tm-feature40': '','sv4-feature28': '','sv4-feature29': '','dv4-feature17': '','ti-feature6': '','ti-feature7': '','dv4-feature16': '',
              'dv4-feature19': '','ti-feature8': '','dv4-feature18': '','dv4-feature13': '','sv4-feature33': '','tm-feature38': '','dv4-feature12': '','sv4-feature34': '','tm-feature37': '','dv4-feature15': '',
              'sv4-feature31': '','tm-feature36': '','dv4-feature14': '','sv4-feature32': '','tm-feature35': '','sv4-feature37': '','tm-feature34': '','sv4-feature38': '','tm-feature33': '','dv4-feature11': '',
             'sv4-feature35': '','tm-feature32': '','dv4-feature10': '','sv4-feature36': '','tm-feature31': '','sv4-feature30': '','tm-feature39': '','cr-feature1': '','tz-feature16': '','tz-feature17': '',
            'cr-feature3': '','tz-feature18': '','cr-feature2': '','tz-feature19': '','cr-feature5': '','tz-feature12': '','cr-feature4': '','tz-feature13': '','cr-feature7': '','tz-feature14': '','cr-feature6': '',
            'tz-feature15': '','txl-feature32': '','tm-feature74': '','txl-feature33': '','tm-feature73': '','sv4-feature39': '','txl-feature34': '','tm-feature72': '','txl-feature35': '','tm-feature71': '',
             'txl-feature36': '','tm-feature70': '','txl-feature37': '','txl-feature38': '','sv4-feature42': '','tm-feature69': '','sv4-feature43': '','tm-feature68': '','tm-feature67': '','tm-feature66': '',
            'tm-feature65': '','txl-feature30': '','tm-feature64': '','txl-feature31': '','tz-feature10': '','tz-feature11': '','sv4-feature40': '','sv4-feature41': '','tz-feature27': '','txl-feature29': '',
            'tz-feature28': '','tz-feature29': '','tz-feature23': '','tz-feature24': '','tz-feature25': '','tz-feature26': '','tm-feature63': '','txl-feature21': '','tm-feature62': '','txl-feature22': '','tm-feature61': '',
             'txl-feature23': '','tm-feature60': '','txl-feature24': '','ct-feature17': '','txl-feature25': '','ct-feature18': '','txl-feature26': '','ct-feature19': '','txl-feature27': '','txl-feature28': '',
             'tm-feature59': '','tm-feature58': '','tm-feature57': '','tm-feature56': '','ct-feature20': '','tm-feature55': '','ct-feature21': '','tm-feature54': '','ct-feature22': '','tm-feature53': '','ct-feature23': '',
             'txl-feature20': '','cr-feature9': '','cr-feature8': '','tz-feature20': '','tz-feature21': '','tz-feature22': '','txl-feature18': '','txl-feature19': '','txl-feature10': '','txl-feature11': '','txl-feature12': '',
             'txl-feature13': '','txl-feature14': '','txl-feature15': '','txl-feature16': '','txl-feature17': '','te-feature9': '','te-feature8': '','te-feature7': '','te-feature6': '','cr-feature32': '','sp-feature12': '',
             'te-feature5': '','cr-feature31': '','sp-feature11': '','te-feature4': '','cr-feature30': '','sp-feature10': '','te-feature3': '','te-feature2': '','cr-feature36': '','sp-feature16': '','te-feature1': '',
             'cr-feature35': '','sp-feature15': '','cr-feature34': '','sp-feature14': '','cr-feature33': '','sp-feature13': '','cr-feature39': '','cr-feature38': '','cr-feature37': '','txl-feature3': '','txl-feature4': '',
             'txl-feature1': '','txl-feature2': '','cr-feature19': '','txl-feature7': '','txl-feature8': '','txl-feature5': '','txl-feature6': '','txl-feature9': '','cr-feature21': '','cr-feature20': '','cr-feature25': '',
             'cr-feature24': '','cr-feature23': '','cr-feature22': '','cr-feature29': '','cr-feature28': '','cr-feature27': '','cr-feature26': '','tm-feature30': '','dv4-feature27': '','tm-feature27': '','dv4-feature24': '',
             'tm-feature26': '','dv4-feature23': '','tm-feature25': '','dv4-feature26': '','tm-feature24': '','dv4-feature25': '','tm-feature23': '','dv4-feature20': '','cr-feature10': '','tm-feature22': '','tm-feature21': '',
             'dv4-feature22': '','tm-feature20': '','dv4-feature21': '','cr-feature14': '','cr-feature13': '','cr-feature12': '','cr-feature11': '','cr-feature18': '','cr-feature17': '','tm-feature29': '','cr-feature16': '',
             'tm-feature28': '','cr-feature15': '','sp-feature8': '','sp-feature9': '','sp-feature6': '','sp-feature7': '','tm-feature16': '','tm-feature15': '','tm-feature14': '','tm-feature13': '','tm-feature12': '',
             'tm-feature11': '','tm-feature10': '','sp-feature1': '','sp-feature4': '','sp-feature5': '','tm-feature19': '','sp-feature2': '','tm-feature18': '','sp-feature3': '','tm-feature17': '','im-feature3': '',
             'im-feature4': '','im-feature1': '','im-feature2': '','tm-feature4': '','sc-feature16': '','tm-feature5': '','sc-feature17': '','tm-feature2': '','sc-feature14': '','tm-feature3': '','sc-feature15': '',
             'tm-feature8': '','sc-feature12': '','tm-feature9': '','sc-feature13': '','tm-feature6': '','sc-feature10': '','tm-feature7': '','sc-feature11': '','tm-feature1': '','a-feature2': '','a-feature3': '',
             'sc-feature20': '','a-feature4': '','a-feature5': '','a-feature6': '','a-feature7': '','a-feature8': '','a-feature9': '','sc-feature25': '','sc-feature23': '','sc-feature24': '','sc-feature21': '',
             'a-feature1': '','sc-feature22': '','sc-feature18': '','sc-feature19': '','sr-feature5': '','sr-feature4': '','sr-feature7': '','sr-feature6': '','sr-feature1': '','sr-feature3': '','sr-feature2': '',
             'sr-feature9': '','sr-feature8': '','te-feature10': '','te-feature12': '','te-feature11': '','te-feature14': '','te-feature13': '','te-feature16': '','te-feature15': '','ct-feature6': '','ct-feature7': '',
             'ct-feature8': '','ct-feature9': '','ct-feature2': '','ct-feature3': '','ct-feature4': '','ct-feature5': '','ct-feature1': '','te-feature21': '','te-feature20': '','te-feature23': '','te-feature22': '',
             'te-feature25': '','te-feature24': '','te-feature27': '','te-feature26': '','te-feature18': '','lz-feature11': '','te-feature17': '','lz-feature10': '','te-feature19': '','lz-feature19': '','lz-feature18': '',
             'lz-feature17': '','lz-feature16': '','lz-feature15': '','lz-feature14': '','lz-feature13': '','lz-feature12': '','te-feature30': '','te-feature32': '','te-feature31': '','te-feature34': '','te-feature33': '',
             'te-feature36': '','te-feature35': '','sv4-feature11': '','te-feature29': '','sv4-feature12': '','te-feature28': '','lz-feature20': '','sv4-feature10': '','sv4-feature15': '','sv4-feature16': '','sv4-feature13': '',
             'sv4-feature14': '','ml-feature19': '','ml-feature10': '','ml-feature18': '','ml-feature17': '','ml-feature16': '','ml-feature15': '','ml-feature14': '','ml-feature13': '','ml-feature12': '','ml-feature11': '',
             'tz-feature4': '','al-feature21': '','tz-feature3': '','al-feature20': '','tz-feature6': '','tz-feature5': '','al-feature25': '','al-feature24': '','tz-feature2': '','al-feature23': '','tz-feature1': '',
             'al-feature22': '','tz-feature8': '','th-feature10': '','tz-feature7': '','th-feature11': '','th-feature12': '','tz-feature9': '','th-feature13': '','op-feature90': '','op-feature92': '','op-feature91': '',
             'op-feature87': '','op-feature86': '','op-feature89': '','op-feature88': '','op-feature83': '','op-feature82': '','op-feature85': '','op-feature84': '','op-feature81': '','op-feature80': '','op-feature79': '',
             'op-feature76': '','op-feature75': '','op-feature78': '','op-feature77': '','op-feature72': '','op-feature71': '','op-feature74': '','op-feature73': '','op-feature70': '','op-feature69': '','op-feature68': '',
             'op-feature65': '','op-feature64': '','op-feature67': '','op-feature66': '','op-feature61': '','op-feature60': '','op-feature63': '','op-feature62': '','th-feature14': '','op-feature58': '','th-feature15': '',
             'op-feature57': '','th-feature16': '','th-feature17': '','op-feature59': '','th-feature18': '','op-feature54': '','th-feature19': '','op-feature53': '','op-feature56': '','op-feature55': '','op-feature50': '',
             'op-feature52': '','op-feature51': '','al-feature10': '','al-feature14': '','al-feature13': '','al-feature12': '','al-feature11': '','al-feature18': '','al-feature17': '','al-feature16': '','th-feature20': '',
             'al-feature15': '','th-feature21': '','th-feature22': '','th-feature23': '','th-feature24': '','al-feature19': '','th-feature25': '','op-feature47': '','th-feature26': '','op-feature46': '','th-feature27': '',
             'op-feature49': '','op-feature48': '','th-feature28': '','op-feature43': '','th-feature29': '','op-feature42': '','op-feature45': '','op-feature44': '','op-feature41': '','op-feature40': '','op-feature36': '',
             'op-feature35': '','op-feature38': '','op-feature37': '','op-feature32': '','op-feature31': '','op-feature34': '','op-feature33': '','al-feature3': '','sc-feature8': '','al-feature2': '','sc-feature7': '',
             'al-feature1': '','op-feature30': '','sc-feature6': '','sc-feature5': '','sc-feature4': '','sc-feature3': '','sc-feature2': '','sc-feature1': '','th-feature8': '','th-feature7': '','th-feature6': '',
             'th-feature5': '','th-feature9': '','th-feature4': '','op-feature39': '','th-feature3': '','th-feature2': '','th-feature1': '','op-feature25': '','op-feature24': '','op-feature27': '','op-feature26': '',
             'op-feature21': '','op-feature20': '','op-feature23': '','op-feature22': '','al-feature9': '','al-feature8': '','al-feature7': '','al-feature6': '','al-feature5': '','al-feature4': '','sc-feature9': '',
             'op-feature29': '','op-feature28': '','op-feature14': '','op-feature13': '','op-feature16': '','op-feature15': '','op-feature10': '','op-feature12': '','op-feature11': '','lz-feature9': '','lz-feature8': '',
             'lz-feature7': '','cr-feature50': '','op-feature18': '','op-feature17': '','op-feature19': '','ml-feature8': '','ml-feature9': '','lz-feature6': '','lz-feature5': '','lz-feature4': '','lz-feature3': '',
             'lz-feature2': '','cr-feature43': '','lz-feature1': '','cr-feature42': '','cr-feature41': '','cr-feature40': '','cr-feature47': '','cr-feature46': '','ml-feature1': '','cr-feature45': '','ml-feature2': '',
             'cr-feature44': '','ml-feature3': '','ml-feature4': '','ml-feature5': '','cr-feature49': '','ml-feature6': '','cr-feature48': '','ml-feature7': '','op-feature9': '','op-feature8': '','op-feature7': '',
             'op-feature6': '','op-feature5': '','op-feature4': '','op-feature3': '','op-feature2': '','op-feature1': '','a-feature10': '','tm-feature84': '','a-feature11': '','tm-feature83': '','a-feature12': '',
             'tm-feature82': '','a-feature13': '','tm-feature81': '','a-feature14': '','tm-feature80': '','a-feature15': '','a-feature16': '','ml-feature43': '','ml-feature42': '','ml-feature41': '','ml-feature40': '',
             'tm-feature79': '','sr-feature23': '','tm-feature78': '','sr-feature22': '','tm-feature77': '','tm-feature76': '','sr-feature24': '','tm-feature75': '','sr-feature21': '','sr-feature20': '','sv4-feature1': '',
             'sv4-feature9': '','sv4-feature8': '','sv4-feature7': '','sv4-feature6': '','sv4-feature5': '','sv4-feature4': '','sr-feature19': '','sv4-feature3': '','sv4-feature2': '','ml-feature32': '','sr-feature16': '',
             'ml-feature31': '','sr-feature15': '','ml-feature30': '','sr-feature18': '','sr-feature17': '','sr-feature12': '','sr-feature11': '','sr-feature14': '','sr-feature13': '','ml-feature39': '','ml-feature38': '',
             'sr-feature10': '','ml-feature37': '','ml-feature36': '','ml-feature35': '','ml-feature34': '','ml-feature33': '','dv4-feature9': '','dv4-feature7': '','dv4-feature8': '','dv4-feature5': '','dv4-feature6': '',
             'dv4-feature3': '','dv4-feature4': '','dv4-feature1': '','dv4-feature2': '','ml-feature21': '','ml-feature20': '','ml-feature29': '','ml-feature28': '','ml-feature27': '','ml-feature26': '','ml-feature25': '',
             'ml-feature24': '','ml-feature23': '','ml-feature22': ''}

data_2 = {'tz_feature38': '','tz_feature34': '','tz_feature35': '','tz_feature36': '','tz_feature37': '','tm_feature52': '','sv4_feature19': '','tm_feature51': '','tm_feature50': '','sv4_feature17': '',
              'sv4_feature18': '','sv4_feature22': '','ct_feature13': '','tm_feature49': '','sv4_feature23': '','ct_feature14': '','tm_feature48': '','sv4_feature20': '','ct_feature15': '','tm_feature47': '',
              'sv4_feature21': '','ct_feature16': '','tm_feature46': '','sv4_feature26': '','tm_feature45': '','sv4_feature27': '','ct_feature10': '','tm_feature44': '','sv4_feature24': '','ct_feature11': '',
              'tm_feature43': '','sv4_feature25': '','ct_feature12': '','tm_feature42': '','tz_feature30': '','tz_feature31': '','tz_feature32': '','tz_feature33': '','ti_feature2': '','ti_feature3': '','ti_feature4': '',
              'ti_feature5': '','ti_feature1': '','tm_feature41': '','tm_feature40': '','sv4_feature28': '','sv4_feature29': '','dv4_feature17': '','ti_feature6': '','ti_feature7': '','dv4_feature16': '',
              'dv4_feature19': '','ti_feature8': '','dv4_feature18': '','dv4_feature13': '','sv4_feature33': '','tm_feature38': '','dv4_feature12': '','sv4_feature34': '','tm_feature37': '','dv4_feature15': '',
              'sv4_feature31': '','tm_feature36': '','dv4_feature14': '','sv4_feature32': '','tm_feature35': '','sv4_feature37': '','tm_feature34': '','sv4_feature38': '','tm_feature33': '','dv4_feature11': '',
             'sv4_feature35': '','tm_feature32': '','dv4_feature10': '','sv4_feature36': '','tm_feature31': '','sv4_feature30': '','tm_feature39': '','cr_feature1': '','tz_feature16': '','tz_feature17': '',
            'cr_feature3': '','tz_feature18': '','cr_feature2': '','tz_feature19': '','cr_feature5': '','tz_feature12': '','cr_feature4': '','tz_feature13': '','cr_feature7': '','tz_feature14': '','cr_feature6': '',
            'tz_feature15': '','txl_feature32': '','tm_feature74': '','txl_feature33': '','tm_feature73': '','sv4_feature39': '','txl_feature34': '','tm_feature72': '','txl_feature35': '','tm_feature71': '',
             'txl_feature36': '','tm_feature70': '','txl_feature37': '','txl_feature38': '','sv4_feature42': '','tm_feature69': '','sv4_feature43': '','tm_feature68': '','tm_feature67': '','tm_feature66': '',
            'tm_feature65': '','txl_feature30': '','tm_feature64': '','txl_feature31': '','tz_feature10': '','tz_feature11': '','sv4_feature40': '','sv4_feature41': '','tz_feature27': '','txl_feature29': '',
            'tz_feature28': '','tz_feature29': '','tz_feature23': '','tz_feature24': '','tz_feature25': '','tz_feature26': '','tm_feature63': '','txl_feature21': '','tm_feature62': '','txl_feature22': '','tm_feature61': '',
             'txl_feature23': '','tm_feature60': '','txl_feature24': '','ct_feature17': '','txl_feature25': '','ct_feature18': '','txl_feature26': '','ct_feature19': '','txl_feature27': '','txl_feature28': '',
             'tm_feature59': '','tm_feature58': '','tm_feature57': '','tm_feature56': '','ct_feature20': '','tm_feature55': '','ct_feature21': '','tm_feature54': '','ct_feature22': '','tm_feature53': '','ct_feature23': '',
             'txl_feature20': '','cr_feature9': '','cr_feature8': '','tz_feature20': '','tz_feature21': '','tz_feature22': '','txl_feature18': '','txl_feature19': '','txl_feature10': '','txl_feature11': '','txl_feature12': '',
             'txl_feature13': '','txl_feature14': '','txl_feature15': '','txl_feature16': '','txl_feature17': '','te_feature9': '','te_feature8': '','te_feature7': '','te_feature6': '','cr_feature32': '','sp_feature12': '',
             'te_feature5': '','cr_feature31': '','sp_feature11': '','te_feature4': '','cr_feature30': '','sp_feature10': '','te_feature3': '','te_feature2': '','cr_feature36': '','sp_feature16': '','te_feature1': '',
             'cr_feature35': '','sp_feature15': '','cr_feature34': '','sp_feature14': '','cr_feature33': '','sp_feature13': '','cr_feature39': '','cr_feature38': '','cr_feature37': '','txl_feature3': '','txl_feature4': '',
             'txl_feature1': '','txl_feature2': '','cr_feature19': '','txl_feature7': '','txl_feature8': '','txl_feature5': '','txl_feature6': '','txl_feature9': '','cr_feature21': '','cr_feature20': '','cr_feature25': '',
             'cr_feature24': '','cr_feature23': '','cr_feature22': '','cr_feature29': '','cr_feature28': '','cr_feature27': '','cr_feature26': '','tm_feature30': '','dv4_feature27': '','tm_feature27': '','dv4_feature24': '',
             'tm_feature26': '','dv4_feature23': '','tm_feature25': '','dv4_feature26': '','tm_feature24': '','dv4_feature25': '','tm_feature23': '','dv4_feature20': '','cr_feature10': '','tm_feature22': '','tm_feature21': '',
             'dv4_feature22': '','tm_feature20': '','dv4_feature21': '','cr_feature14': '','cr_feature13': '','cr_feature12': '','cr_feature11': '','cr_feature18': '','cr_feature17': '','tm_feature29': '','cr_feature16': '',
             'tm_feature28': '','cr_feature15': '','sp_feature8': '','sp_feature9': '','sp_feature6': '','sp_feature7': '','tm_feature16': '','tm_feature15': '','tm_feature14': '','tm_feature13': '','tm_feature12': '',
             'tm_feature11': '','tm_feature10': '','sp_feature1': '','sp_feature4': '','sp_feature5': '','tm_feature19': '','sp_feature2': '','tm_feature18': '','sp_feature3': '','tm_feature17': '','im_feature3': '',
             'im_feature4': '','im_feature1': '','im_feature2': '','tm_feature4': '','sc_feature16': '','tm_feature5': '','sc_feature17': '','tm_feature2': '','sc_feature14': '','tm_feature3': '','sc_feature15': '',
             'tm_feature8': '','sc_feature12': '','tm_feature9': '','sc_feature13': '','tm_feature6': '','sc_feature10': '','tm_feature7': '','sc_feature11': '','tm_feature1': '','a_feature2': '','a_feature3': '',
             'sc_feature20': '','a_feature4': '','a_feature5': '','a_feature6': '','a_feature7': '','a_feature8': '','a_feature9': '','sc_feature25': '','sc_feature23': '','sc_feature24': '','sc_feature21': '',
             'a_feature1': '','sc_feature22': '','sc_feature18': '','sc_feature19': '','sr_feature5': '','sr_feature4': '','sr_feature7': '','sr_feature6': '','sr_feature1': '','sr_feature3': '','sr_feature2': '',
             'sr_feature9': '','sr_feature8': '','te_feature10': '','te_feature12': '','te_feature11': '','te_feature14': '','te_feature13': '','te_feature16': '','te_feature15': '','ct_feature6': '','ct_feature7': '',
             'ct_feature8': '','ct_feature9': '','ct_feature2': '','ct_feature3': '','ct_feature4': '','ct_feature5': '','ct_feature1': '','te_feature21': '','te_feature20': '','te_feature23': '','te_feature22': '',
             'te_feature25': '','te_feature24': '','te_feature27': '','te_feature26': '','te_feature18': '','lz_feature11': '','te_feature17': '','lz_feature10': '','te_feature19': '','lz_feature19': '','lz_feature18': '',
             'lz_feature17': '','lz_feature16': '','lz_feature15': '','lz_feature14': '','lz_feature13': '','lz_feature12': '','te_feature30': '','te_feature32': '','te_feature31': '','te_feature34': '','te_feature33': '',
             'te_feature36': '','te_feature35': '','sv4_feature11': '','te_feature29': '','sv4_feature12': '','te_feature28': '','lz_feature20': '','sv4_feature10': '','sv4_feature15': '','sv4_feature16': '','sv4_feature13': '',
             'sv4_feature14': '','ml_feature19': '','ml_feature10': '','ml_feature18': '','ml_feature17': '','ml_feature16': '','ml_feature15': '','ml_feature14': '','ml_feature13': '','ml_feature12': '','ml_feature11': '',
             'tz_feature4': '','al_feature21': '','tz_feature3': '','al_feature20': '','tz_feature6': '','tz_feature5': '','al_feature25': '','al_feature24': '','tz_feature2': '','al_feature23': '','tz_feature1': '',
             'al_feature22': '','tz_feature8': '','th_feature10': '','tz_feature7': '','th_feature11': '','th_feature12': '','tz_feature9': '','th_feature13': '','op_feature90': '','op_feature92': '','op_feature91': '',
             'op_feature87': '','op_feature86': '','op_feature89': '','op_feature88': '','op_feature83': '','op_feature82': '','op_feature85': '','op_feature84': '','op_feature81': '','op_feature80': '','op_feature79': '',
             'op_feature76': '','op_feature75': '','op_feature78': '','op_feature77': '','op_feature72': '','op_feature71': '','op_feature74': '','op_feature73': '','op_feature70': '','op_feature69': '','op_feature68': '',
             'op_feature65': '','op_feature64': '','op_feature67': '','op_feature66': '','op_feature61': '','op_feature60': '','op_feature63': '','op_feature62': '','th_feature14': '','op_feature58': '','th_feature15': '',
             'op_feature57': '','th_feature16': '','th_feature17': '','op_feature59': '','th_feature18': '','op_feature54': '','th_feature19': '','op_feature53': '','op_feature56': '','op_feature55': '','op_feature50': '',
             'op_feature52': '','op_feature51': '','al_feature10': '','al_feature14': '','al_feature13': '','al_feature12': '','al_feature11': '','al_feature18': '','al_feature17': '','al_feature16': '','th_feature20': '',
             'al_feature15': '','th_feature21': '','th_feature22': '','th_feature23': '','th_feature24': '','al_feature19': '','th_feature25': '','op_feature47': '','th_feature26': '','op_feature46': '','th_feature27': '',
             'op_feature49': '','op_feature48': '','th_feature28': '','op_feature43': '','th_feature29': '','op_feature42': '','op_feature45': '','op_feature44': '','op_feature41': '','op_feature40': '','op_feature36': '',
             'op_feature35': '','op_feature38': '','op_feature37': '','op_feature32': '','op_feature31': '','op_feature34': '','op_feature33': '','al_feature3': '','sc_feature8': '','al_feature2': '','sc_feature7': '',
             'al_feature1': '','op_feature30': '','sc_feature6': '','sc_feature5': '','sc_feature4': '','sc_feature3': '','sc_feature2': '','sc_feature1': '','th_feature8': '','th_feature7': '','th_feature6': '',
             'th_feature5': '','th_feature9': '','th_feature4': '','op_feature39': '','th_feature3': '','th_feature2': '','th_feature1': '','op_feature25': '','op_feature24': '','op_feature27': '','op_feature26': '',
             'op_feature21': '','op_feature20': '','op_feature23': '','op_feature22': '','al_feature9': '','al_feature8': '','al_feature7': '','al_feature6': '','al_feature5': '','al_feature4': '','sc_feature9': '',
             'op_feature29': '','op_feature28': '','op_feature14': '','op_feature13': '','op_feature16': '','op_feature15': '','op_feature10': '','op_feature12': '','op_feature11': '','lz_feature9': '','lz_feature8': '',
             'lz_feature7': '','cr_feature50': '','op_feature18': '','op_feature17': '','op_feature19': '','ml_feature8': '','ml_feature9': '','lz_feature6': '','lz_feature5': '','lz_feature4': '','lz_feature3': '',
             'lz_feature2': '','cr_feature43': '','lz_feature1': '','cr_feature42': '','cr_feature41': '','cr_feature40': '','cr_feature47': '','cr_feature46': '','ml_feature1': '','cr_feature45': '','ml_feature2': '',
             'cr_feature44': '','ml_feature3': '','ml_feature4': '','ml_feature5': '','cr_feature49': '','ml_feature6': '','cr_feature48': '','ml_feature7': '','op_feature9': '','op_feature8': '','op_feature7': '',
             'op_feature6': '','op_feature5': '','op_feature4': '','op_feature3': '','op_feature2': '','op_feature1': '','a_feature10': '','tm_feature84': '','a_feature11': '','tm_feature83': '','a_feature12': '',
             'tm_feature82': '','a_feature13': '','tm_feature81': '','a_feature14': '','tm_feature80': '','a_feature15': '','a_feature16': '','ml_feature43': '','ml_feature42': '','ml_feature41': '','ml_feature40': '',
             'tm_feature79': '','sr_feature23': '','tm_feature78': '','sr_feature22': '','tm_feature77': '','tm_feature76': '','sr_feature24': '','tm_feature75': '','sr_feature21': '','sr_feature20': '','sv4_feature1': '',
             'sv4_feature9': '','sv4_feature8': '','sv4_feature7': '','sv4_feature6': '','sv4_feature5': '','sv4_feature4': '','sr_feature19': '','sv4_feature3': '','sv4_feature2': '','ml_feature32': '','sr_feature16': '',
             'ml_feature31': '','sr_feature15': '','ml_feature30': '','sr_feature18': '','sr_feature17': '','sr_feature12': '','sr_feature11': '','sr_feature14': '','sr_feature13': '','ml_feature39': '','ml_feature38': '',
             'sr_feature10': '','ml_feature37': '','ml_feature36': '','ml_feature35': '','ml_feature34': '','ml_feature33': '','dv4_feature9': '','dv4_feature7': '','dv4_feature8': '','dv4_feature5': '','dv4_feature6': '',
             'dv4_feature3': '','dv4_feature4': '','dv4_feature1': '','dv4_feature2': '','ml_feature21': '','ml_feature20': '','ml_feature29': '','ml_feature28': '','ml_feature27': '','ml_feature26': '','ml_feature25': '',
             'ml_feature24': '','ml_feature23': '','ml_feature22': ''}

def parse(url):
    data_re = {}
    try:
        data = getjson(url)
        data_info = json.loads(data.text)
        data_con = data_info['body']['tianji_api_userportrait_modelv3_response']
        if len(data_con) == 571:
            data_1.update(data_con)
            data_1_1 = data_1
        if len(data_con) == 641:
            data_1_1 = data_con
        for i in range(len(data_2)):
            data_re[list(data_2.keys())[i]] = list(data_1_1.values())[i]
        logger.info('{}解析成功'.format(url))
    except Exception as e:
        logger.error('{}**中止** ERROR: {} '.format(url, e))
    data_all = {"version":"v","model":"user portrait","result":data_re}
    data_re_1 = json.dumps(data_all)
    return data_re_1

if __name__ == '__main__':
    LOG_PATH = '{}'.format(os.path.abspath(os.getcwd()))
    logger = create_logger(LOG_PATH)
    url = 'http://hzed-com.oss-cn-shenzhen.aliyuncs.com/risk/rong360Model/a33ee9a8-3792-487f-9222-be99e7d7ad2a.txt'
    res = parse(url)
    print(res)



