__author__ = 'nimbus'

class Statistic(object):

    def __init__(self, *args, **kwargs):
        print("$$$$$$$$$$$$$$$$$$$")
        print(args[0])

        self.stat_wp = args[0]['wp']
        self.stat_crawler = args[0]['crawler']

        if self.stat_wp:
            self.wordpress()

        if self.stat_crawler:
            self.crawler()

    def __path__(self):
        import sys
        sys.path.append(self)

    def __del__(self):
        print(self.__class__.__name__, "Destroyed")
        return self

    def crawler(self):
        return print("stats about this Crawler")

    def wordpress(self):
        from veryprettytable import VeryPrettyTable

        x = VeryPrettyTable()
        x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
        x.add_row(["Adelaide",1295, 1158259, 600.5])
        x.add_row(["Brisbane",5905, 1857594, 1146.4])
        x.add_row(["Darwin", 112, 120900, 1714.7])
        x.add_row(["Hobart", 1357, 205556, 619.5])
        x.add_row(["Sydney", 2058, 4336374, 1214.8])
        x.add_row(["Melbourne", 1566, 3806092, 646.9])
        x.add_row(["Perth", 5386, 1554769, 869.4])
        return print(x)
