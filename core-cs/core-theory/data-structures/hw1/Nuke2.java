import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Nuke2 {

    /**
     * 
     * 
     * 
     * 
     * @param arg is not used.
     * @throws IOException
     *                     thrown if there are any problems parsing the
     *                     user's input.
     */
    public static void main(String[] arg) throws IOException {
        try {
            String input = new BufferedReader(new InputStreamReader(System.in)).readLine();
            if ("".equals(input) || input.length() < 2) {
                throw new IOException("Input cannot be '' or input cannot have len < 2");
            } else {
                String begin, end;
                begin = input.substring(0, 1);
                end = input.substring(2);
                System.out.println(begin + end);

            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }

    }
}
