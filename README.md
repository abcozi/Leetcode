# Leetcode

### Solution to 167. Two Sum II - Input array is sorted(Easy)
#### 一、使用語言: Python3 <br>
#### 二、Runtime & Memory Usage <br>
Runtime: 56 ms, faster than <b> 96.89% </b> of Python3 online submissions for Two Sum II - Input array is sorted. <br>
Memory Usage: 13.3 MB, less than <b> 100.00% </b> of Python3 online submissions for Two Sum II - Input array is sorted. <br>
 
#### 三、解題邏輯<br>
	使用兩個pointer，初始分別指向陣列頭尾。外層迴圈處理「頭指針」的向後移動，內層迴圈處理「尾指針」的向前移動。
內層迴圈的持續條件有二個，第一個為兩個pointer指向的陣列值的加總「大於目標值」，第二個為頭指針必須在尾指針之前，迴圈內每一輪會把尾指針往前移動一格，使加總值越來越小，以更靠近目標值。一旦發現加總值「<=」目標值，表示偉指針往前過頭了，因此內層迴圈會停止。
外層迴圈的持續條件為頭指針小於陣列長度，每一輪會將頭指針往後移一格，使加總值越來越大，以靠近目標值。一旦發現加總值等於目標值，即return頭尾指針的位置。
