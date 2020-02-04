import java.util.Comparator;

public class Student {
    private int id = 0;
    private String name = "Default name";
    private String address = "Default Addrress";
    private double cgpa = 0.0;

    public Student(int id, String name, String address, double cgpa) {
        this.id = id;
        this.name = name;
        this.address = address;
        this.cgpa = cgpa;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public double getCgpa() {
        return cgpa;
    }

    public void setCgpa(double cgpa) {
        this.cgpa = cgpa;
    }

    public static Comparator<Student> nameCompare = new Comparator<Student>() {

        public int compare(Student s1, Student s2) {
            String name1 = s1.getName();
            String name2 = s2.getName();
            return name1.compareTo(name2);
        }
    };

    public static Comparator<Student> sIdNo = new Comparator<Student>() {

        public int compare(Student s1, Student s2) {

            int sId1 = s1.getId();
            int sId2 = s2.getId();

            return sId1 - sId2;

        }
    };

    @Override
    public String toString() {
        return "[Student name is " + getName() + ", ID is " + getId() + ", Address is " + getAddress() + ", CGPA is " + getCgpa() + "]\n";
    }

}
