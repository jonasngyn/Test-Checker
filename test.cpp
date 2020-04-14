#include <bits/stdc++.h>
#include <algorithm>
#define JN Jonasngyn
#define pb push_back
#define FOR(i, a, b) for(int i = int(a); i <= int(b); i++)
#define FORD(i, a, b) for(int i = int(a); i >= int(b); i--)
#define REP(i, r) for(int i = 0; i < r; i++)
#define FAST ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define READFILE freopen("input.txt", "r", stdin)
#define WRITEFILE freopen("output.txt", "w", stdout);
#define ii pair<int, int>
#define ll long long
#define fi first
#define se second
using namespace std;

const int MAXN=3e5+6;
int A,B,m, minA=9999999, minB=9999999;
int a[MAXN], b[MAXN], ans=9999999;


int main()
{
    #ifndef ONLINE_JUDGE
        READFILE;
        WRITEFILE;
    #endif
    // FAST;
    
 	cin >> A >> B >>m;
 	FOR(i,1,A) {cin >> a[i]; minA=min(minA,a[i]);}
 	FOR(i,1,B) {cin >> b[i]; minA=min(minB,b[i]);}
 	FOR(i,1,m){
 		int u,v,Cost;
 		cin >> u >> v >> Cost;
 		ans=min(ans,a[u]+b[v]-Cost);
 	}
 	cout<<max(0,min(ans,minA+minB));
    return 0;
}
