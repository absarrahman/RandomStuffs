import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class StudentRecord {
    ArrayList<Student> StudentArray = new ArrayList<Student>();
    Scanner input = new Scanner(System.in);

    //Adds record

    public void addRecord() {
        if (StudentArray.isEmpty()) {
            System.out.println("Enter ID");
            int studentID = input.nextInt();
            input.nextLine();
            System.out.println("Enter name ");
            String studentName = input.nextLine();
            System.out.println("Enter address");
            String studentAddress = input.nextLine();
            System.out.println("Enter CGPA");
            double studentCgpa = input.nextDouble();
            Student studentObj = new Student(studentID, studentName, studentAddress, studentCgpa);
            StudentArray.add(studentObj);
            System.out.println("Record added successfully");
        } else {
            boolean flag = false;
            System.out.println("Enter ID");
            int studentID = input.nextInt();

            //Checks all objects

            for (int i = 0; i < StudentArray.size(); i++) {

                if (studentID == StudentArray.get(i).getId()) {
                    flag = true;
                    break;
                }
            }

            //check if exits or not

            if (!flag) {
                input.nextLine();
                System.out.println("Enter name ");
                String studentName = input.nextLine();
                System.out.println("Enter address");
                String studentAddress = input.nextLine();
                System.out.println("Enter CGPA");
                double studentCgpa = input.nextDouble();
                Student studentObj = new Student(studentID, studentName, studentAddress, studentCgpa);
                StudentArray.add(studentObj);
                System.out.println("Record added successfully");
            } else {
                System.out.println("ID exists");
            }
        }
    }

    //deletes record

    public void deleteRecord() {
        System.out.println("Enter id");
        int studentID = input.nextInt();
        int count = 0;
        for (int i = 0; i < StudentArray.size(); i++) {
            if (studentID == StudentArray.get(i).getId()) {
                StudentArray.remove(i);
                ++count;
            }
        }
        if (count == 0) {
            System.out.println(studentID + " does not exist");
        } else {
            System.out.println(studentID + " is deleted");
        }
    }

    //Edit student record

    public void editRecord() {
        System.out.println("Enter ID of the student for editing information");
        int studentID = input.nextInt();
        int count = 0;
        for (int i = 0; i < StudentArray.size(); i++) {
            if (studentID == StudentArray.get(i).getId()) {
                input.nextLine();
                System.out.println("Enter new name");
                StudentArray.get(i).setName(input.nextLine());
                System.out.println("Enter new address");
                StudentArray.get(i).setAddress(input.nextLine());
                System.out.println("Enter new CGPA");
                StudentArray.get(i).setCgpa(input.nextDouble());
                ++count;
            }
        }
        if (count == 0) {
            System.out.println(studentID + " does not exist");
        }
    }

    //Print record

    public void printRecord() {
        for (int i = 0; i < StudentArray.size(); i++) {
            for (int j = i + 1; j < StudentArray.size(); j++) {
                if (StudentArray.get(i).getName().compareTo(StudentArray.get(j).getName()) != 0) {
                    Collections.sort(StudentArray, Student.nameCompare);
                }

            }
            for (int j = i + 1; j < StudentArray.size(); j++) {
                if (StudentArray.get(i).getName().compareTo(StudentArray.get(j).getName()) == 0) {
                    Collections.sort(StudentArray, Student.sIdNo);
                }
            }

        }

        for (Student obj : StudentArray) {
            System.out.println(obj);
        }

    }
}


