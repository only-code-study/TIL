#include <iostream>
#include <algorithm> 
#include <vector>

using namespace std;

int n;
int cacheLen[501], cacheCnt[501], S[500];

const int MAX = 20000000 + 1;

int lis(int start) {
	int& ret = cacheLen[start + 1];
	if(ret != -1) return ret;
	
	ret = 1;
	for(int next = start + 1; next < n; ++next)
		if(start == -1 || S[start] < S[next])
			ret = max(ret, lis(next + 1));
	return ret;
}

int count(int start) {
	if(lis(start) == 1) return 1;
	int& ret = cacheCnt[start + 1];
	if(ret != -1) return ret;
	ret = 0;
	for(int next = start + 1; next < n; ++next) {
		if((start == -1 || S[start] < S[next]) && lis(start) == lis(next) + 1)
			ret = min<long long>(MAX, (long long)ret + count(next));
	}
	return ret;
}

int cache[501];

int lis3(int start) {
    int& ret = cache[start+1];
    if(ret != -1) return ret;
    ret = 1;
    for(int next = start+1; next < n; ++next)
        if(start == -1 || S[start] < S[next])
            ret = max(ret, lis3(next) + 1);
    return ret;
}

void reconstruct (int start, int skip, vector<int>& lis) {
    if(start != -1) lis.push_back(S[start]);

    vector<pair<int, int> > followers;
    for(int next = start + 1; next < n; ++next)
        if((start == 1 || S[start] < S[next]) && lis3(start) == lis3(next) + 1)
            followers.push_back(make_pair(S[next], next));
    sort(followers.begin(), followers.end());

    for(int i = 0; i < followers.size(); ++i) {
        int idx = followers[i].second;
        int cnt = count(idx);
        if(cnt <= skip)
            skip -= cnt;
        else {
            reconstruct(idx, skip, lis);
            break;
        }
    }
}

int main()
{
	int C, n, k;
	cin >> C;
	for(int i = 0; i < C; i++) {
		cin >> n >> k;
		for (int j = 0; j < n; j++) {
			cin >> S[j];
		} 
		cout << reconstruct(0, k, cache) << endl;
	} 
}
