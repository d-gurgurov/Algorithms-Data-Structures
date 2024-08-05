# Algorithms and Data Structures Solutions

Welcome to the **Algorithms and Data Structures Solutions** repository! This repository is dedicated to providing clear and concise solutions to some of the most popular problems in Data Structures and Algorithms (DSA). Each solution (in src) is accompanied by detailed explanations to help me understand the underlying concepts and improve my problem-solving skills. 

This repo is created exclusively for educational purposes. 

## Table of Contents

| Category      | Name                  | Level                         | Notes                 |
|---------------|-----------------------|------------------------------|-----------------------|
| Arrays        | [Two Sum](https://leetcode.com/problems/two-sum/)               |     Easy          | use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice;  |
| Linked Lists  | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)   |  Easy | find local min and search for local max, sliding window;               |
| Trees         | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)    |       Easy        | hashset to get unique values in array, to check for duplicates easily |
| Sorting       | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)      |      Medium         | pattern: prev subarray cant be negative, dynamic programming: compute max sum for each prefix           |
| String      | [Valid Parantheses](https://leetcode.com/problems/valid-parentheses/description/)      |      Easy         | push opening brace on stack, pop if matching close brace, at end if stack empty, return true;           |