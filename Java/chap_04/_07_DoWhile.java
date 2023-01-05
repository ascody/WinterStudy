package chap_04;
public class _07_DoWhile {
    public static void main(String[] args) {
        // 반복문 do while
        int distance = 25; // 전체 거리 25m
        int move = 0; // 현재 이동 거리 0m
        int height = 2; // 키 2m
        while (move + height < distance){
            System.out.println("발차기를 계속합니다.");
            System.out.println("현재 이동 거리 : " + move);
            move += 3;
        }
        System.out.println("도착하였습니다.");

        System.out.println(" --- 반복문 #1 --- ");

        // 키가 엄청나게 큰 사람
        distance = 25; // 전체 거리 25m
        move = 0; // 현재 이동 거리 0m
        height = 25; // 키 25m
        while (move + height < distance){
            System.out.println("발차기를 계속합니다.");
            System.out.println("현재 이동 거리 : " + move);
            move += 3;
        }
        System.out.println("도착하였습니다.");

        System.out.println(" --- 반복문 #2 --- ");

        // do while 반복문
        do {
            System.out.println("발차기를 계속합니다.");
            System.out.println("현재 이동 거리 : " + move);
            move += 3;
        } while (move + height < distance);
            System.out.println("도착하였습니다.");
    }
}
