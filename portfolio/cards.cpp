#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
string getNumber(int x);
string getSuit(int x);
string getTotal(int x);


int main()
{
    bool keepgoing = true;
    int rando;
    string suitguess, number;
    vector<int> cards;
    for (int i = 1; i <= 52; i++)
    {
        cards.push_back(i);
    }
    random_shuffle(cards.begin(), cards.end());
    rando = cards.back();  
    cards.pop_back();
    cout << "Welcome to the Card Guessing Game!" << endl;

    cout << "What Suit Will the Card Be? (Diamonds, Clubs, Spades, Hearts): ";
    cin >> suitguess;
    cout << "What kind of card to you think it will be? (Ace, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King): ";
    cin >> number;

    cout << "You guessed the " << number << " of " << suitguess;
    cout << endl;
    cout << "The card drawn was the " << getTotal(rando);
    cout << endl;
}

string getNumber(int x)
{
    switch(x % 13)
    {
        case 0:
        return "Ace";
        case 1:
        return "2";
        case 2: 
        return "3";        
        case 3:
        return "4";
        case 4:
        return "5";
        case 5: 
        return "6"; 
        case 6:
        return "7";
        case 7:
        return "8";
        case 8: 
        return "9";
        case 9:
        return "10";
        case 10:
        return "Jack";
        case 11: 
        return "Queen";
        case 12:
        return "King";
    }
}

string getSuit(int x)
{
    string NewSuit;
    if ( x <= 12 )
    {
        NewSuit = "Hearts";
    }
    if ( x >= 13 && x <= 25  )
    {
        NewSuit = "Spades";
    }    
    if ( x >= 26 && x <= 38  )
    {
        NewSuit = "Diamonds";
    }    
    if ( x >= 39 && x <= 52 )
    {
        NewSuit = "Clubs";
    }

    return NewSuit;

}

string getTotal(int x)
{
    string together = getNumber(x) + " of " + getSuit(x);
    return together;
}

