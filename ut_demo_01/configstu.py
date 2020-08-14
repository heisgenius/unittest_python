import configparser
class readConfig:
    def readconfig(self,filepath,section,option):
        cf = configparser.ConfigParser()
        cf.read(filepath,encoding='utf-8')
        res = cf.get(section,option)
        return res
#
# if __name__ == '__main__':
#     res =readConfig().readconfig('testcase.conf','option','caseid')
#     print(type(res))