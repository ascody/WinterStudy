package chap_10;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class _Quiz_10 {
    public static void main(String[] args) {

        ArrayList<Customer> customer = new ArrayList<>();
        customer.add(new Customer("챈들러", 50));
        customer.add(new Customer("레이첼", 42));
        customer.add(new Customer("모니카", 21));
        customer.add(new Customer("벤자민", 18));
        customer.add(new Customer("제임스", 5));

        System.out.println("미술관 입장료");
        System.out.println("--------------");
        customer.stream().map(x -> x.age >= 20 ? x.name + " 5000원": x.name + " 무료").forEach(System.out::println);
    }
}
class Customer{
    String name;
    int age;
    Customer(String name, int age){
        this.name = name;
        this.age = age;
    }
}