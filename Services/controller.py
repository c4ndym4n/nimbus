__author__ = 'nimbus'

class System(object):

    def __init__(self):
        self.name = "System Object"
        self.passed = False

    def check_updates(self):
        """
        Check online for available updates
        :return:
        """
        pass

    def check_startup(self):
        """
        Check Installed component
        :return:
        """
        pass

    def check_mongo(self):
        """
        Check if MongoDB Server is running
        :return: True/False
        """
        pass

if __name__ == '__main__':

    # Check IF HomeBrew is installed
    # Check IF Python is installed
    # Check IF MongoDB is installed
    # Check IF weeChat is installed


    obj = {'test': True, 'test2': False, 'test3': True}

    for v in obj.values():
        if v:
            print("Test is True")
        elif not v:
            print("Something is False")