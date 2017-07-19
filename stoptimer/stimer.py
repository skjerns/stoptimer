import time

class sTimer:

    def __init__(self, identifier = ''):
        self.starttime = dict()
        self.start(identifier)

    def start(self, identifier = ''):
        self.starttime[identifier] = time.time()
        
    def stop(self, identifier = ''):
        
        try:
            end = time.time()-self.starttime[identifier]
            if end > 7200:
                hours   = end//3600
                minutes = end//60 - hours*60
                print("Elapsed{}: {:.0f}:{:02.0f} hours".format(' ' + str(identifier) if len(str(identifier))>0 else '',hours,minutes))
            elif end > 180:
                minutes = end//60
                seconds = end%60
                print("Elapsed{}: {:.0f}:{:02.0f} minutes".format(' ' + str(identifier) if len(str(identifier))>0 else '', minutes , seconds ))
            else:
                print("Elapsed{}: {:02.3f} seconds".format('Timer ' + str(identifier) if len(str(identifier))>0 else '',end))
            return  time.time()-self.starttime[identifier]
        
        except KeyError:
            print('Identifier {} not found'.format(identifier))
       
