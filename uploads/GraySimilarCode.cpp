//Jai Shri Radhe Krishna
//Jai Shri Ram

#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;

#define vi      vector<ll>
#define vvi     vector<vi>
#define vs      vector<string>
#define vb      vector<bool>
#define vvb     vector<vb>
#define all(x)  (x).begin(),(x).end()
#define allr(x) (x).rend(),(x).rbegin()
#define pb      emplace_back
#define mp      make_pair
#define pii     pair<ll,ll>
#define vpii    vector<pii>
#define ff      first
#define ss      second
#define sz(x)   ((int)(x).size())
#define inf     1e18
#define mod     (((int)1e9))
#define mod1    998244353
#define w(x)    int x; cin>>x; while(x--)
#define endl    '\n'

#ifndef ONLINE_JUDGE
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#else
#define debug(x)
#endif

void _print(ll t) {cerr << t;}
void _print(int t) {cerr << t;}
void _print(string t) {cerr << t;}
void _print(char t) {cerr << t;}
void _print(lld t) {cerr << t;}
void _print(double t) {cerr << t;}
void _print(ull t) {cerr << t;}

template <class T, class V> void _print(pair <T, V> p);
template <class T> void _print(vector <T> v);
template <class T> void _print(set <T> v);
template <class T, class V> void _print(map <T, V> v);
template <class T> void _print(multiset <T> v);
template <class T, class V> void _print(pair <T, V> p) {cerr << "{"; _print(p.ff); cerr << ","; _print(p.ss); cerr << "}";}
template <class T> void _print(vector <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(set <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(multiset <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T, class V> void _print(map <T, V> v) {cerr << "[ "; for (auto i : v) {_print(i); cerr << " ";} cerr << "]";}


typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>
PBDS; // find_by_order(return iterator to kth largest element) ,order_of_key(no of elements which are strictly less than k)

void file_i_o() {
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#ifndef ONLINE_JUDGE
	freopen("Error.txt", "w", stderr);
#endif
}


template<class T> vector<vector<T>> genrateSubsets(T *arr, ll n) {vector<vector<T>> ans((1 << n)); for (ll i = 0; i < (1 << n); i++) {ll j = i; ll d = 0; while (j > 0) {int lasBit = (j & 1); if (lasBit == 1)ans[i].push_back(arr[d]); d++; j = j >> 1;}} return ans ;}
bool isOdd(ll n) {return n & 1;}
int getBit(ll n, ll i) {return (n & (1 << i) ) > 0;}
ll setBit(ll n, ll i) {return (n | (1 << i));}
ll clearBit(ll n , ll i) {return (n & (~(1 << i)));}
ll updateBit(ll n, ll i, int v) {n = clearBit(n, i); return (n | (v << i));}
ll clearLastIBits(ll n, ll i) {return (n & (-1 << i));}
ll clearRangeIToJ (ll n, ll i, ll j) {return (n & ((-1 << j + 1) | (1 << i) - 1));}
ll countSetBit (ll n) {return __builtin_popcount(n);}
string decimalTobinary(ll n) {string ans = ""; while (n > 0) {if (n & 1)ans = '1' + ans; else ans = '0' + ans; n = n >> 1;} return ans;}
//string to char array use strcpy(char array name, stringname.c_str())
void stringMultiply(int *a, int &n, int no) {int carry = 0; for (int i = 0; i < n; i++) {int product = a[i] * no + carry; a[i] = product % 10; carry = product / 10;} while (carry) {a[n] = carry % 10; carry = carry / 10; n++;}}

//------------------ Matrix Exponentiation Code ----------------------------//
// k in the number of terms in LR
// b matrix stores the values of function when it is less than k
// c matrix stores the values of the coefficent of terms in the LR
// vvi matrix_multiply(vvi A, vvi B) {
//  vvi C(k + 1, vector<ll>(k + 1));
//  for (int i = 1; i <= k; i++) {
//      for (int j = 1; j <= k; j++) {
//          for (int x = 1; x <= k; x++)
//              C[i][j] = (C[i][j] + (A[i][x] * B[x][j]) % mod) % mod;
//      }
//  }
//  return C;
// }

// vvi matrix_pow(vvi A, ll p) {
//  if (p == 1)
//      return A;
//  if (p & 1)
//      return matrix_multiply(A, matrix_pow(A, p - 1));
//  vvi X = matrix_pow(A, p / 2);
//  return matrix_multiply(X, X);
// }

// ll compute(ll n) {
//  if (n == 0)
//      return 0;
//  if (n <= k) {
//      return b[n - 1];
//  }
//  // otherwise use matrix exponentiation
//  vi F1(k + 1); // indexing from 1
//  for (int i = 1; i <= k; i++)
//      F1[i] = b[i - 1];
//  // The transformation matrix
//  vvi T(k + 1, vector<ll>(k + 1));
//  for (int i = 1; i <= k; i++) {
//      for (int j = 1; j <= k; j++) {
//          if (i < k) {
//              if (j == i + 1)
//                  T[i][j] = 1;
//          }
//          else
//              T[i][j] = c[k - j];
//      }
//  }

//  T = matrix_pow(T, n - 1);
//  ll res = 0;
//  for (int i = 1; i <= k; i++)
//      res = (res + (T[1][i] * F1[i]) % mod) % mod;
//  return res;
// }

void solve() {
	int n; cin >> n;
	vi arr(n);
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	if (n >= 130) {
		cout << "Yes";
		return;
	}
	else {
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				for (int k = j + 1; k < n; k++) {
					for (int l = k + 1; l < n; l++) {
						ll x = arr[i] ^ arr[j] ^ arr[k] ^ arr[l];
						if (x == 0) {
							cout << "Yes";
							return ;
						}
					}
				}
			}
		}
	}
	cout << "No";
}

int main() {
	file_i_o();

//  w(t)
	solve();

	return 0;
}