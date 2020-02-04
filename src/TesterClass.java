import java.util.Scanner;

public class TesterClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StudentRecord student = new StudentRecord();
        while (true) {

            System.out.println("Enter 0 to Quit");
            System.out.println("Enter 1 to Add a Record");
            System.out.println("Enter 2 to Print the Records");
            System.out.println("Enter 3 to Delete a Record");
            System.out.println("Enter 4 to Edit a Record");

            int promptNumber = sc.nextInt();
            switch (promptNumber) {
                case 1:
                    student.addRecord();
                    break;
                case 2:
                    student.printRecord();
                    break;
                case 3:
                    student.deleteRecord();
                    break;
                case 4:
                    student.editRecord();
                    break;
                default:
                    System.out.println("Wrong input. Enter correct choice");
                    break;
                case 0:
                    return;
            }

        }
    }
}