''' Module containing class with functionality to test number of open apps. '''
import psutil
import pkgutil
import time
import platform, os

from PySide.QtGui import QMessageBox
if pkgutil.find_loader('PyQt5'):
    from PyQt5.QtCore import Qt
elif pkgutil.find_loader('PyQt4'):
    from PyQt4.QtCore import Qt
elif pkgutil.find_loader('PySide'):
    from PySide.QtCore import Qt
else:
    print("You don't seem to have a QT library installed;"
              " please install PyQT or PySide.")
    exit(1)

from com_resources import logger

class NumOfAppOpen(QMessageBox):
    RESTRICTED_APPS = {'chrome','firefox','skype'}
    KILLING_COMMAND = {
        'Linux': "kill -9 {}",
        'Darwin': "kill -9 {}",
        'Windows': "Taskkill /PID {} /F"
    }
    OS_NAME = platform.system()

    def __init__(self,parent=None):
        super(NumOfAppOpen,self).__init__(parent)
        
    def process_exists(self):
        open_res_proc, len_open_res, process_ids = self.get_res_open_processes()
        # Give a delay in case the process is in closing phase
        # if len_open_res != 0:
        #     time.sleep(4)
        #     open_res_proc, len_open_res = self.get_res_open_processes()
        if len_open_res != 0:
            # Create a string containing name of all open apps
            # Show maximum of 5 apps.
            # if  self.OS_NAME == 'Windows':
            #     command_to_stop = self.KILLING_COMMAND[self.OS_NAME]
            #     for process in open_res_proc:
            #         os.system(command_to_stop.format(process_ids[process]))
            apparent_index = (len_open_res, 5)[len_open_res > 5] - 1
            apps_string = ''.join(
                open_res_proc[apparent_index])       
            if len_open_res > 5:
                apps_string += '...'
            return self.prompt_for_closing_apps(apps_string)
    
    def get_res_open_processes(self):
        ''' Function to get all the open processes that are restricted. '''
        open_apps = set()
        process_ids = {}
        logger.error('in thread {} is This:'.format(self.__class__) )
        logger.error("hello i am in thread Run Function")
        for proc in psutil.process_iter():
            try:
                proc_name = proc.name()
                if proc_name != u"":
                    logger.error(proc.name)
                    app_name = proc_name.split('.')[0]
                    process_ids[app_name] = proc.pid            
                    open_apps.add(app_name)
                    #print (proc.cmdline())
            except psutil.AccessDenied:
                logger.error("Permission error or access denied on process")
            # Collect all the open apps
        # Get the open apps that are restricted in list
        process_list = list(self.RESTRICTED_APPS.intersection(open_apps))
        return process_list, len(process_list), process_ids

    def prompt_for_closing_apps(self, apps_string):
        ''' Function to prompt user for prompting user
        for closing the restricted apps. '''
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)       
        msg.setInformativeText("Kindly Close The Application")
        msg.setWindowTitle("ERROR!!!")
        msg.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint) #added by RSR
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)            
        msg.setText("Looks like  application {} is Open".format(apps_string.upper()))
        msg.show()
        msg.exec_()
        return True