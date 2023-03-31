import Gcode


class ReadFile:
    cont = 0

    @staticmethod
    def read():
        try:
            file = open("katownik-01.ncp", 'r')

            topology_list = file.readlines()
            for i in topology_list:
                #print(i)
                if i == "(<Contour>)":
                    ReadFile.cont += 1
                if i[0] == 'N':
                    Gcode.Gcode.gcode_parse(i)
            file.close()
        except FileNotFoundError as e:
            print(f"FileNotFoundError successfully handled\n"f"{e}")
