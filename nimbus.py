__author__ = 'nimbus'

# TODO: Create Basic Crawler
# TODO: Create MasScanner
# TODO: Create Plugins
# TODO: Plugin: Gmail
# TODO: Create System
# TODO: System: [ check for ] Update
# TODO: System: Encryption and Decryption
# TODO: Thread Control System
# TODO: CommandLineInterface

# MOST IMPORTANT
# TODO: Threading
# TODO: Services
# TODO: Modules
# TODO: Plugins
# TODO: Body/Framework
# TODO: Documentation System Pythonic

if __name__ == '__main__':
    from Core import controller



    try:
        app = controller.Framework()
    except KeyboardInterrupt as k:
        print("\n\n\t*** [ KEYBOARD INTERRUPT ] ***\n\n")
