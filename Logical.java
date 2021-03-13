public class Logical {
    int inputProblemOne;
    long perfectNumber;

    public Logical() {
    }

    Logical(int inputProblemOne) {
        this.inputProblemOne = inputProblemOne;
        perfectNumber = 0;
    }

    void problemOne() {
        int summatory = 0;
        if (inputProblemOne <= 0) {
            return;
        } else if (inputProblemOne <= 9)
            summatory = inputProblemOne;
        else{
            String inputStr = inputProblemOne + "";
            for(int i = 0; i < inputStr.length(); i++){
                summatory += Integer.parseInt(inputStr.charAt(i) + "");
                if(summatory>10)
                    return;
            }
        }
        perfectNumber = (summatory == 10 ? inputProblemOne : Long.parseLong(inputProblemOne + ((10 - summatory) + "")));
    }

    public static void main(String[] args) {
        Logical log = new Logical(19);
        log.problemOne();
        System.out.print("The perfect number is: ");
        System.out.print(log.perfectNumber==0 ? "The input isn't a perfect number." : log.perfectNumber);
        System.out.println();
        //compile and execute:  javac Logical.java && java Logical
        //output:               The perfect number is: 19
    }
}