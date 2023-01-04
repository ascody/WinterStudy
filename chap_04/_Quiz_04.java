package chap_04;
public class _Quiz_04 {
    public static void main(String[] args) {
        int hour = 10;
        int carFee = 4000 * hour;
        int max = 30000;
        boolean common = false;
        if (carFee > 30000)
            carFee = 30000;
        if(!common)
            carFee /= 2;
        System.out.println("주차 요금: " + carFee + "원");
    }
}