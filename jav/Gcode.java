import java.util.HashMap;

import static java.lang.Math.*;

public class Gcode {

    static double pi = 3.14159265359;
    static float posx;
    static float posy;
    static double res = 0;
    static HashMap<Character, Float> numbers = new HashMap<>();
    public static void gcode_parse(String data){

        char lett = 'Q';
        StringBuilder num = new StringBuilder();
        for (int i = 0; i < data.length(); i++) {

            char c = data.charAt(i);
            if(c >= 'A' && c <= 'Z') {
                if(num.length() != 0){
                    float f=Float.parseFloat(String.valueOf(num));
                    numbers.put(lett, f);
                }
                lett = c;
                num = new StringBuilder();

            }
            if( (c >= '0' && c <= '9') || (c == '.') ){
                num.append(c);
            }
        }
        float f=Float.parseFloat(String.valueOf(num));
        numbers.put(lett, f);

        //System.out.println("Contour: " + ReadFile.cont + " " + numbers);

        Float g = numbers.get('G');
        if (g == 0.0) {
            g0();
        } else if (g == 1.0) {
            g1();
        } else if (g == 2.0) {
            g2();
        } else if (g == 3.0) {
            g3();
        }
    }
    public static void g0(){
        posx = numbers.get('X');
        posy = numbers.get('Y');
    }
    public static void g1(){
        float difx = numbers.get('X') - posx;
        float dify = numbers.get('Y') - posy;
        posx = numbers.get('X');
        posy = numbers.get('Y');
        double re = pow(difx, 2) + pow(dify, 2);
        res += sqrt(re);
        System.out.println("g1 " + sqrt(re));
    }
    public static void g2(){
        float difx = numbers.get('X') - posx;
        float dify = numbers.get('Y') - posy;
        posx = numbers.get('X');
        posy = numbers.get('Y');
        double P23 = sqrt(pow(difx, 2) + pow(dify, 2));
        double difxr = numbers.get('I') - posx;
        double difyr = numbers.get('J') - posy;
        double r = sqrt(pow(difxr, 2) + pow(difyr, 2));
        double per = 2*pi*r;
        double ang = toDegrees(acos((pow(r, 2) + pow(r, 2) - pow(P23, 2)) / (2 * r * r)));
        res += (360 - ang) * per / 360;

        System.out.println("g2 " + ang * per / 360);
    }
    public static void g3(){
        float difx = numbers.get('X') - posx;
        float dify = numbers.get('Y') - posy;
        posx = numbers.get('X');
        posy = numbers.get('Y');
        double P23 = sqrt(pow(difx, 2) + pow(dify, 2));
        double difxr = numbers.get('I') - posx;
        double difyr = numbers.get('J') - posy;
        double r = sqrt(pow(difxr, 2) + pow(difyr, 2));
        double per = 2*pi*r;
        double ang = toDegrees(acos((pow(r, 2) + pow(r, 2) - pow(P23, 2)) / (2 * r * r)));
        res += ang * per / 360;

        System.out.println("g3 " + ang * per / 360);
    }
}
