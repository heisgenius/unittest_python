import logging
class myLog:
    def mylog(self):
        # 创建一个收集器
        mylogger = logging.getLogger('快递信息')

        formmater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                                       datefmt='%Y-%m-%d %H:%M:%S %p',)
        # 设置收集的级别
        mylogger.setLevel('DEBUG')
        # 创建一个输出渠道（控制台）
        ch = logging.StreamHandler()
        # 设置输出的级别
        ch.setLevel('INFO')
        ch.setFormatter(formmater)
        fh = logging.FileHandler('快递信息.txt',encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formmater)
        # 将收集器与输出渠道关联起来
        mylogger.addHandler(ch)
        mylogger.addHandler(fh)
# mylogger.debug('12312313')
# mylogger.info('12312313')
# mylogger.warning('12312313')
# mylogger.error('12312313')
# mylogger.critical('12312313')
