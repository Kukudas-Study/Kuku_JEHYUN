import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] smalls = new int[9];
		int tmp  = 0;
		// 난쟁이 채워넣고 tmp에 전체 합 저장
		for (int i = 0; i < 9; i++) {
			smalls[i] = sc.nextInt();
			tmp += smalls[i];
		}
        	// 오름차순 정렬하기
		for (int i = 0; i < 8; i++) {
			for (int j = i; j < 9; j++) {
				if(smalls[i]>smalls[j]) {
					int temp = smalls[i];
					smalls[i] = smalls[j];
					smalls[j] = temp;
				}
			}
		}
        
		boolean isDone = false;
		// 2개씩 묶어서 100이 되는지 확인하고 된다면 바로 2중 반복 탈출
       	 	for (int i = 0; i < 8; i++) {
			for (int j = i; j < 9; j++) {
				if(tmp-smalls[i]-smalls[j] == 100) {
                    			// 물론 탈출전에 해당 value 값 -1로 초기화
					smalls[i] = -1;
					smalls[j] = -1;
					isDone = true;
					break;
				}
			}
			if (isDone) {
				break;
			}
		}
        	// 출력
		for (int i : smalls) {
			if (i > 0) {
				System.out.println(i);
			}
		}
	}

}
