import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Objects;
import java.util.Scanner; // Import the Scanner class to read text files

public class ReadFile {

    static int cont = 0;
    public static void read() {
        try {
            File myObj = new File("D:\\jakub.kaleta\\isys\\dlugosc_ciecia\\katownik-01.ncp");
            Scanner myReader = new Scanner(myObj);

            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                //System.out.println(data);
                if(Objects.equals(data, "(<Contour>)")){
                    cont += 1;
                }/*
                if(data.charAt(0) == 'N'){
                    Gcode.gcode_parse(data);
                }*/
                // System.out.println(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}