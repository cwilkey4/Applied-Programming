#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <vector>
#include <deque>

using namespace std;

int main() 
{
    string file = "tasks.txt";
    string choice = "0";
    
    while (choice != "4")
    {
        
        cout << "ToDo" << endl;
        cout << "1. View Tasks" << endl;
        cout << "2. Add New Task" << endl;
        cout << "3. Complete Task" << endl;
        cout << "4. Quit" << endl;
        cout << "What do you want to do?" << endl;
        cin >> choice;
        
        // 1. View
        if (choice == "1")
        {
            ifstream viewFile(file);
            string task;
            cout << "Tasks:" << endl;
            while (getline(viewFile, task))
            {
                cout << task << endl;
            }
            

            viewFile.close();
        }

        // 2. Add
        if (choice == "2")
        {
            cout << "What task are you adding?" << endl;
            string newTask;
            cin >> newTask;

            ofstream writeFile(file, ios::app);
            writeFile << newTask << endl;
            writeFile.close();
        }

        // 3. Complete
        if (choice == "3")
        {
            ifstream readFile(file);

            vector<string> tasks;
            string task;

            cout << "Tasks:" << endl;
            while (getline(readFile, task))
            {
                cout << task << endl;
            }
            readFile.close(); 

            cout << "Which task do you want to complete?" << endl;
            string completedTask;
            cin.ignore();
            getline(cin, completedTask);

            readFile.open(file); 
            bool taskExists = false;
            while (getline(readFile, task))
            {
                if (task == completedTask)
                {
                    taskExists = true;
                }
                else
                {
                    tasks.push_back(task);
                }
            }
            readFile.close();

            if (!taskExists)
            {
                cout << "That task wasn't found in the ToDo list." << endl;
            }
            else
            {
                cout << "Congrats! You're done!" << endl;
            }

            ofstream writeFile(file);

            for (const string &t : tasks)
            {
                writeFile << t << endl;
            }
            writeFile.close();

        }

    }
}