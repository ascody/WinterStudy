package chap_13;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class _Quiz_13 {
    public static void main(String[] args) {
        String path = "C:\\Users\\acre2\\IdeaProjects\\JavaWorkspace\\src\\chap_13\\saying.txt";
        Scanner sc = new Scanner(System.in);
        System.out.println("속담 퀴즈 입니다. 빈 칸에 알맞은 말을 입력하시오. (주관식)");
        System.out.println("-------------------------------------------------");

        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line;
            while (true) {
                line = br.readLine();
                if (line == null)
                    break;
                System.out.println("(문제) " + line);
                System.out.print("정답 입력 => ");
                String answer = sc.next();
                line = br.readLine();
                if (line.equals(answer))
                    System.out.println("정답입니다!!!");
                else
                    System.out.println("틀렸습니다. 정답은 " + line + "입니다.");
                System.out.println();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        System.out.println("-------------------------------------------------");
        System.out.println("모든 퀴즈가 완료되었습니다.\n수고하셨습니다. ^^");
    }
}
