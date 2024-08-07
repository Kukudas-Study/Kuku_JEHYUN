import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int[][] paper = new int[1001][1001];
		// 부분 탐색에 필요한 부분
//		int[][] range = new int[n][4];
		
		for (int i = 1; i < n+1; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			
			// 부분 탐색에 필요한 부분
//			range[i-1] = new int[]{x, y, w, h};
			
			for (int j = y; j < y+h; j++) {
				for (int k = x; k < x+w; k++) {
					paper[j][k] = i;
				}
			}
			
		}
		// 완전 탐색 코드
		for (int i = 1; i < n+1; i++) {
			int count = 0;
			for (int j = 0; j < 1001; j++) {
				for (int k = 0; k < 1001; k++) {
					if (paper[j][k] == i) {
						count += 1;
					};
				}
			}			
			System.out.println(count);
		}
		// 부분 탐색 코드
//		for (int i = 1; i < n+1; i++) {
//			int count = 0;
//			for (int j = range[i-1][1]; j < range[i-1][1] + range[i-1][3]; j++) {
//				for (int k = range[i-1][0]; k < range[i-1][0] + range[i-1][2]; k++) {
//					if (paper[j][k] == i) {
//						count += 1;
//					};
//				}
//			}			
//			System.out.println(count);
//		}
		
	
	}
}