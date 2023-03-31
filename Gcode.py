import math


class Gcode:
    pi = 3.14159265359
    posx = 0
    posy = 0
    res = 0
    numbers = {}

    @staticmethod
    def gcode_parse(data):

        lett = 'Q'
        num = ""
        i = 0
        while i < len(data):
            c = data[i]
            if 'A' <= c <= 'Z':
                if len(num) != 0:
                    f = float(str(num))
                    Gcode.numbers[lett] = f
                lett = c
                num = ""

            if ('0' <= c <= '9') or (c == '.'):
                num += c
            i += 1
        f = float(str(num))
        Gcode.numbers[lett] = f

        # System.out.println("Contour: " + ReadFile.cont + " " + numbers)

        g = Gcode.numbers['G']
        if g == 0.0:
            Gcode.g0()
        elif g == 1.0:
            Gcode.g1()
        elif g == 2.0:
            Gcode.g2()
        elif g == 3.0:
            Gcode.g3()

    @staticmethod
    def g0():
        Gcode.posx = Gcode.numbers['X']
        Gcode.posy = Gcode.numbers['Y']

    @staticmethod
    def g1():
        difx = Gcode.numbers['X'] - Gcode.posx
        dify = Gcode.numbers['Y'] - Gcode.posy
        Gcode.posx = Gcode.numbers['X']
        Gcode.posy = Gcode.numbers['Y']
        re = difx ** 2 + dify ** 2
        Gcode.res += math.sqrt(re)
        print("g1 " + str(math.sqrt(re)))

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
        ang = math.degrees(math.acos((r ** 2 + r ** 2 - P23 ** 2) / (2 * r * r)))
        Gcode.res += (360 - ang) * per / 360

        print("g2 " + str(ang * per / 360))

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
        ang = math.degrees(math.acos((r ** 2 + r ** 2 - P23 ** 2) / (2 * r * r)))
        Gcode.res += ang * per / 360

        print("g3 " + str(ang * per / 360))
