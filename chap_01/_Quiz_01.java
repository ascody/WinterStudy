package chap_01;
public class _Quiz_01 {
    public static void main(String[] args) {
        // 버스 도착 정보 출력 프로그램
        // 버스 번호 : "1234", "상암08"
        // 남은 시간 분 단위 : 3분, 5분
        // 남은 거리 km 단위 : 1.5km, 0.8km

        String busNum = "상암08";
        int minuteRemain = 3;
        double distRemain = 1.2;

        System.out.println(busNum + "번 버스");
        System.out.println("약 " + minuteRemain + "분 후 도착");
        System.out.println("남은 거리 " + distRemain + "km");
    }
}
