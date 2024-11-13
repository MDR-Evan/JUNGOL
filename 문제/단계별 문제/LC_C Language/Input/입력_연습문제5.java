public class 입력_연습문제5 {
    public static void main(String[] args) {
        float x = 1.2340f, y = 10.3459f;

        System.out.println("전체 7자리로 맞추고 소수 4자리까지 출력");
        System.out.printf("x = %7.4f\n",x);
        System.out.printf("y = %7.4f\n\n",y);
        System.out.println("소수 2자리까지 출력(반올림)");
        System.out.printf("x = %.2f\n",x);
        System.out.printf("y = %.2f\n",y);
    }
}
