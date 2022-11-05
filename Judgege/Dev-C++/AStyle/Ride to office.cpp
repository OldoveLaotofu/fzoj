#include<bits/stdc++.h>
using namespace std;
int main() {
	int n,temv,temt,maxv,max_t;
	while(1) {
		maxv=-1;
		max_t=0;
		scanf("%d",&n);
		if(n==0) {
			break;
		}
		for(int i=0; i<n; i++) {
			scanf("%d%d",&temv,&temt);
			if(maxv<temv&&temt>=0) {
				maxv=temv;
				max_t=temt;
			}
		}
		printf("%.0llf\n",ceil(4500*1.0/maxv*3.6+max_t));
	}
	return 0;
}
