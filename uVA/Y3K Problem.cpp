#include <iostream>
#include <cstdio>
using namespace std;

int months[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

bool isLeap(int y){
    if (y % 400 == 0) return true;
    return (y % 4 == 0) && (y % 100 != 0);
}

int dateToDays(int d, int m, int y){
    int r = 0;
    for (int i = 1;i<y;i++){
        r += isLeap(i) ? 366 : 365;
    }
    //r += 365 * y + int((y - 1) / 4) - int((y - 1) / 100) + int((y - 1) / 400);
    for (int i = 0;i<m - 1;i++){
        r += months[i];
    }
    if (isLeap(y) && m > 2) r++;
    r += d;
    return r;
}

void printOutput(int days) {
 
    int year = 1;
    int month = 1;
 
    while(days >= 365) {
        days -= (isLeap(year) ? 366 : 365);
 
        if (days <= 0) {
            days += (isLeap(year) ? 366 : 365);
            break;
        }
 
        year++;
    }
 
    if (days) {
 
        if (isLeap(year)) months [1]++;
 
        while (days > months [month - 1]) {
            days -= months [month - 1];
            month++;
        }
    }
 
    printf ("%d %d %d\n", days, month, year);
 
}

int main(){
    int futureDays;
    int day;
    int month;
    int year;
 
    while (scanf ("%d %d %d %d", &futureDays, &day, &month, &year)) {
        if ( futureDays == 0 && day == 0 && month == 0 && year == 0 ) break;
 
        months[1] = 28;
 
        int totalNumberOfDays = dateToDays(day, month, year);
        totalNumberOfDays += futureDays;
        printOutput(totalNumberOfDays);
    }
 
    return 0;
}