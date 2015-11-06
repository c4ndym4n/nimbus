__author__ = 'nimbus'
from time import sleep
import argparse

def usage(session_name=None):

    line = "*" * 40

    print("\n\tCommand [Option] [<args>]\n\n\tThe Options you can choose from are:\n\t%s\n\r" % line)
    commands = {"set": "set to something",
              "config": "config something",
              "stats": "config something"}
    for k in commands.keys(): print("\t{}\t\t\t{}".format(k, commands[k]))
    print("\n\r")

def sprint(string):
    print("nimbus \> %s" % string)


class Framework(object):

    def __init__(self):

        self.session_name = "nimbus \> "
        self.session_state = True
        self.session_id = ""
        self.function_name = ""

        self.parser = argparse.ArgumentParser(prog="Nimbus Framework", description="Need it any description?", argument_default=None, epilog="Nimbus // Rain with Rage, Exploit with Love")
        self.parser.add_argument('command', help="Use command to begin")


        while self.session_state:
            self.command = input(self.session_name)
            if not self.command:
                sprint("No Command Given")
                continue
            else:
                self.args = self.parser.parse_args(self.command.split()[0:1])
                try:
                    if hasattr(self, self.args.command):
                        getattr(self, self.args.command)()
                    elif not hasattr(self, self.args.command):
                        sprint("Unrecognized command")
                        sprint("try again pall")
                        sleep(1), usage()
                        print("*" * 40), self.parser.print_help()

                        continue
                except Exception as e:
                    print("[ EXCEPTION ]", str(e))


    def __str__(self):
        print(self.__dict__)

    def __del__(self):
        print(self.__class__.__name__, "Destroyed")
        return self

    def run(self):
        print("Command to Run the arguments")
        print(self.args)

    def config(self):
        print("Config Command")

    def db(self):
        self.function_name = "db"
        stats_parser = argparse.ArgumentParser(prog="Db function", description="This is a description for the Database",
                                         usage=usage(self.function_name))
        while self.session_state:
            if not self.command.split()[1:]:
                break
            elif self.command.split()[1:]:
                try:
                    # stats_parser.add_argument("module")
                    stats_parser.add_argument("--start", dest="start", action="store_true", default=False, help="Start the Database")
                    stats_parser.add_argument("--status", dest="status", action="store_true", default=False, help="The Status of the Database")
                    stats_parser.add_argument("--add", dest="add", action="store_true", default=False, help="Add something to the database")
                    stats_parser.add_argument("--dbs", dest="dbs", action="store_true", default=False, help="How many databases are there")
                    stats_parser.add_argument("--pid", dest="pid", action="store_true", default=False, help="Database Process ID")

                except Exception as e:
                    print(Exception("[ STATS ]", str(e)))

                args = stats_parser.parse_args(self.command.split()[1:])

                from Plugins.Stats.controller import Statistic
                # from Plugins import Stats
                stats = Statistic(vars(args))
                break


    def stats(self):
        self.function_name = "stats"
        stats_parser = argparse.ArgumentParser(prog="Stats function", description="This is a description for the Stats",
                                         usage=usage(self.function_name))
        while self.session_state:
            if not self.command.split()[1:]:
                break
            elif self.command.split()[1:]:
                try:
                    # stats_parser.add_argument("module")
                    stats_parser.add_argument("--crawler", dest="crawler", action="store_true", default=False, help="Statistics about the Crawler")
                    stats_parser.add_argument("--wp", dest="wp", action="store_true", default=False, help="Statistics about the found vulnerable WP websites")

                except Exception as e:
                    print(Exception("[ STATS ]", str(e)))

                args = stats_parser.parse_args(self.command.split()[1:])

                from Plugins.Stats.controller import Statistic
                # from Plugins import Stats
                stats = Statistic(vars(args))
                break

    def set(self):
        self.function_name = "set"
        self.set_commands = {}

        parser = argparse.ArgumentParser(prog="Set Function", description="This is a description for the Set function",
                                         usage=usage(self.function_name))
        while self.session_state:
            if not self.command.split()[1:]:
                break
            elif self.command.split()[1:]:
                try:
                    parser.add_argument("-?", dest="?")
                    parser.add_argument("-n", "--name", dest="set_name")
                except Exception as e:
                    raise Exception("[ SET ]", str(e))
                args = parser.parse_args(self.command.split()[1:])

    def service(self):
        self.function_name = "service"
        service_parser = argparse.ArgumentParser(prog="Set Function", description="This is a description for the Set function")

        while self.session_state:
            if not self.command.split()[1:]:
                sprint("You didnt give me any [OPTIONS]")
                sleep(2)
                break
            elif self.command.split()[1:]:
                try:
                    service_parser.add_argument("--up", dest="up")
                    service_parser.add_argument("--all", dest="all")
                    service_parser.add_argument("--mongo", dest="mongo")
                except Exception as e:
                    raise Exception("[ SERVICE ]", str(e))
                args = service_parser.parse_args(self.command.split()[1:])


    def exit(self):
        self.session_state = False
        print("GoodBye")


def main():
    try:
        app = Framework()
    except KeyboardInterrupt as k:
        print("\n\n\t*** [ KEYBOARD INTERRUPT ] ***\n\n")

if __name__ == '__main__':
    main()


    # TODO: When exiting:
    """
    ...saving history...truncating history files...
    ...completed.
    Deleting expired sessions...none found.
    """

if __name__ == '__main__':
    # print(Framework.__dict__)
    main()