import Gcode
import os


class ReadFile:
    cont = 0
    res = 0.0
    resp = 0.0
    part = ''
    @staticmethod
    def read():
        try:
            directory = os.fsencode("D:\jakub.kaleta\isys\dlugosc_ciecia\laser_transfer")
            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                myfile = open(os.path.join(directory.decode("utf-8"), filename), 'r')
                topology_list = myfile.readlines()
                for i in topology_list:
                    if i.find('Contour') == 2:  # (<Contour>)
                        ReadFile.cont = 1
                    if i.find('Contour') == 3:  # (</Contour>)
                        ReadFile.cont = 0
                        # print("Contour: " + format(ReadFile.resp, '.2f') + " Suma: " + format(ReadFile.res, '.2f'))
                        # ReadFile.resp = 0.0
                    if i.find('Plan') == 2:  # (<Plan>)
                        print('==========================================\nFile name: ' + filename)
                        if i.find('JobCode') >= 0:
                            print(i[7:-3])
                    if i.find('Part') == 2:  # (<Part>)
                        ReadFile.part = i[17:-14]
                    if i[0] == 'N':
                        skl = Gcode.Gcode.gcode_parse(i)
                        if ReadFile.cont == 1:
                            # print(skl)
                            ReadFile.res += skl
                            # ReadFile.resp += skl
                    if i.find('Part') == 3:  # (</Part>)
                        print("Part name: " + ReadFile.part + ": " + format(ReadFile.res, '.2f') + " mm")
                        ReadFile.res = 0.0
                        # ReadFile.resp = 0.0
                        ReadFile.cont = 0
                    if i.find('NcpProgram') == 3:
                        print('==========================================\n')
                myfile.close()
        except FileNotFoundError as e:
            print(f"FileNotFoundError successfully handled\n"
                  f"{e}")
