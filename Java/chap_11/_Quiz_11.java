package chap_11;
public class _Quiz_11 {
    public static void main(String[] args) {
        int errorCode = 0;
        try {
            if (errorCode == 0) {
                System.out.println("상품 구매를 완료하였습니다.");
            } else if (errorCode == 1) {
                throw new TimeException("상품 구매 가능 시간이 아닙니다.");
            } else if (errorCode == 2) {
                throw new SoldoutException("해당 상품은 매진되었습니다.");
            }
        } catch (TimeException e) {
            System.out.println(e.getMessage());
            System.out.println("상품 구매는 20시부터 가능합니다.");
        } catch (SoldoutException e) {
            System.out.println(e.getMessage());
            System.out.println("다음 기회에 이용해주세요.");
        }
    }
}
class SoldoutException extends Exception{
    public SoldoutException(String message) { super(message); }
}
class TimeException extends Exception{
    public TimeException(String message) { super(message); }
}
