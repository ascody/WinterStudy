package chap_12;
public class _Quiz_12 {
    public static void main(String[] args) {
        Runnable prepareA = () -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("A 상품 준비 " + i + "/5");
            }
            System.out.println("-- A 상품 준비 완료 --");
        };
        Runnable prepareB = () -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("B 상품 준비 " + i + "/5");
            }
            System.out.println("-- B 상품 준비 완료 --");
        };
        Thread threadA = new Thread(prepareA);
        Thread threadB = new Thread(prepareB);
        threadA.start();
        threadB.start();

        try {
            threadA.join();
            threadB.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        Runnable prepareSet = () -> {
            System.out.println("== 세트 상품 포장 시작 ==");
            for (int i = 1; i <= 5; i++) {
                System.out.println("세트 상품 포장 " + i + "/5");
            }
            System.out.println("== 세트 상품 포장 완료 ==");
        };
        Thread threadSet = new Thread(prepareSet);
        threadSet.start();
    }
}
