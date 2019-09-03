/*

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

*/



class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        
        // create a copy of the original board
        vector<vector<int>> copyBoard = board;
        
        int numRow = board.size();
        int numCol = board[0].size();
        cout << numRow << ", " << numCol << endl;
         
        // copy the board, and use the copied one as the reference
        for (int i=0; i<numRow; i++){
            for (int j=0; j<numCol; j++){
                copyBoard[i][j] = board[i][j];
                cout << copyBoard[i][j] ;
            }
        }
        vector <int> validNei;
        // change the input board
        for (int i=0; i<numRow; i++){
            for (int j=0; j<numCol; j++){
                
                //check the neightbor of copyBoard[i][j]
                if (i-1>=0 && j-1>=0 && copyBoard[i-1][j-1]==1){
                    validNei.push_back(1);
                }
                if (i-1>=0  && copyBoard[i-1][j]==1){
                    validNei.push_back(1);
                }
                if (i-1>=0 && j+1<numCol && copyBoard[i-1][j+1]==1){
                    validNei.push_back(1);
                }
            
                if (j-1>=0 && copyBoard[i][j-1]==1){
                    validNei.push_back(1);
                }
                if (j+1<numCol && copyBoard[i][j+1]==1){
                    validNei.push_back(1);
                }
                
                if (i+1<numRow && j-1>=0 && copyBoard[i+1][j-1]==1){
                    validNei.push_back(1);
                }
                if (i+1<numRow && copyBoard[i+1][j]==1){
                    validNei.push_back(1);
                }
                if (i+1<numRow && j+1<numCol && copyBoard[i+1][j+1]==1)                           {
                    validNei.push_back(1);
                }
                
                
                // cout <<"round "<<i<<","<<j<<":";
                // cout << validNei.size() << endl;
                int n = validNei.size();
                if (n<2 || n>3){
                    board[i][j] = 0;
                }
                if (n==3){
                    board[i][j] = 1;
                }
                // cout << board[i][j] << endl;
                validNei.clear();
            }
            
        }         
    }
};