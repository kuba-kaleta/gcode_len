import math


class Gcode:
    numbers = {}
    pi = 3.14159265359
    posx = 0
    posy = 0
    @staticmethod
    def gcode_parse(data):
        lett = 'Q'
        num = ""
        i = 0
        # Gcode.numbers['I'] = 0.0
        # Gcode.numbers['J'] = 0.0
        # Gcode.numbers['G'] = 0.5
        while i < len(data):
            c = data[i]
            if 'A' <= c <= 'Z':
                if len(num) != 0:
                    f = float(str(num))
                    Gcode.numbers[lett] = f
                lett = c
                num = ""
                if c == 'G':
                    wpisg = True

            if ('0' <= c <= '9') or (c == '.'):
                num += c
            i += 1
        f = float(str(num))
        Gcode.numbers[lett] = f

        g = Gcode.numbers['G']
        if g == 1.0:
            return Gcode.g1()
        elif g == 2.0:
            return Gcode.g2()
        elif g == 3.0:
            return Gcode.g3()
        else:
            Gcode.posx = Gcode.numbers['X']
            Gcode.posy = Gcode.numbers['Y']
            return 0.0

    # @staticmethod
    # def gx():

    @staticmethod
    def g1():
        difx = Gcode.numbers['X'] - Gcode.posx
        dify = Gcode.numbers['Y'] - Gcode.posy
        Gcode.posx = Gcode.numbers['X']
        Gcode.posy = Gcode.numbers['Y']
        re = difx ** 2 + dify ** 2
        return math.sqrt(re)
        # print("g1 " + str(math.sqrt(re)))

    @staticmethod
    def g2():
        difx = Gcode.numbers['X'] - Gcode.posx
        dify = Gcode.numbers['Y'] - Gcode.posy
        Gcode.posx = Gcode.numbers['X']
        Gcode.posy = Gcode.numbers['Y']
        P23 = math.sqrt(difx ** 2 + dify ** 2)
        difxr = Gcode.numbers['I'] - Gcode.posx
        difyr = Gcode.numbers['J'] - Gcode.posy
        r = math.sqrt(difxr ** 2 + difyr ** 2)
        per = 2 * Gcode.pi * r
        arcarg = (r ** 2 + r ** 2 - P23 ** 2) / (2 * r * r)
        if arcarg > 1:
            ang = math.degrees(math.acos(1))
        elif arcarg < -1:
            ang = math.degrees(math.acos(-1))
        else:
            ang = math.degrees(math.acos(arcarg))
        return ang * per / 360
        # print("g3 " + str(ang * per / 360))

    @staticmethod
    def g3():
        difx = Gcode.numbers['X'] - Gcode.posx
        dify = Gcode.numbers['Y'] - Gcode.posy
        Gcode.posx = Gcode.numbers['X']
        Gcode.posy = Gcode.numbers['Y']
        P23 = math.sqrt(difx ** 2 + dify ** 2)
        difxr = Gcode.numbers['I'] - Gcode.posx
        difyr = Gcode.numbers['J'] - Gcode.posy
        r = math.sqrt(difxr ** 2 + difyr ** 2)
        per = 2 * Gcode.pi * r
        arcarg = (r ** 2 + r ** 2 - P23 ** 2) / (2 * r * r)
        if arcarg > 1:
            ang = math.degrees(math.acos(1))
        elif arcarg < -1:
            ang = math.degrees(math.acos(-1))
        else:
            ang = math.degrees(math.acos(arcarg))
        return (360 - ang) * per / 360
        # print("g2 " + str(ang * per / 360))



