#include <iostream>
#include <array>
using namespace std;

array<int, 2> get_ru(int n, int p){
    if(n * n == p){
        array<int, 2> output;
        output = {n / 2 + 1, n / 2 + 1};
        return output;
    }
    int s = 0, l = n, shift = 0;
    while(true){
        s += 4 * (l - 1);
        if(s >= p){
            break;
        }else{
            shift += 1;
            l -= 2;
        }
    }
    int dif =(4 * (l - 1)) - (s - p);
    int step = 1, r = 1, u = 1;
    while(true){
        if(step == 1){
            // nothing
        }else if (2 <= step && step <= l){
            r += 1;
        }else if(l < step && step <= 2 * l - 1){
            u += 1;
        }else if(2*l-1 < step && step <= 3 * l -2){
            r -= 1;
        }else{
            u -= 1;
        }

        if(step == dif){
            array<int, 2> out;
            out = {r + shift, u + shift};
            return out;
        }
        
        step += 1;
    }
}

int main(){
    int n, s, d;
    cin >> n >> s >> d;

    array<int,2> s_ru = get_ru(n, s);
    array<int,2> d_ru = get_ru(n, d);

    cout << "R: " << d_ru[0] - s_ru[0] << endl;
    cout << "U: " << d_ru[1] - s_ru[1] << endl;

}
#Shift = تعداد لایه ای که جابجا شده بود
#S = تعداد اعدادی که تا اون لایه مدنظر ما پوشش میده مثلا لایه اول شانزده تا عدد اول رو پوشش میده
#P = وقتی ی پارامتر میخواییم به تابع پاس بدیم کار تابع پیدا کردن مختصات بود
#N = ضلع مربع
#L = left
#R = right 
#U = up
#Dif = difference
