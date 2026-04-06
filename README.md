Homework: Hash-Something-Out  
Nicholas Munro  
COS 226 

**Attempts**:

1. Started out with a very basic hash function and table. For the hash function I started with just adding the value of the char and % by table size. I used a linked list method for the hash table.  
   1. The method was fast, one of the faster methods I used I believe, but the drawbacks were fairly high collisions and unused space. My table size was 15000, so that definitely had an effect. Clearly my hash function wasn’t dispersing well.

| Unused Space(Title Table) | 11533 |
| :---- | :---- |
| Unused Space(Quote Table) | 11533 |
| Collisions  (Title Table) | 11534 |
| Collisions  (Quote Table) | 12277 |
| Time to complete: | 0.0571 |

2. My second attempt used the same linked list method for the table, but with an updated hash function. For the hash function I multiplied the char value by a prime number, the value of the prime number that it is being multiplied by was based on the index of char. Finally I multiplied the entire string value by the length of the string and % by table size.  
   1. The method was slightly slower but had a marketed reduction in and less wasted space. The table remained the same size as before 15000\. Cleary a better hash function but still not great overall.

| Unused Space(Title Table) | 10281 |
| :---- | :---- |
| Unused Space(Quote Table) | 10281 |
| Collisions  (Title Table) | 10282 |
| Collisions  (Quote Table) | 10946 |
| Time to complete: | 0.08275 |

3. For my third attempt I used the same hashfunction as my second attempt but with a linear probing method for the table. The table size was also increased to 20,000 so that it would be able to hold all elements. The first linear probing method I used was to simply at 1 to the index in a loop till I hit an open index.   
   1. The unused space went way down in this method. However the collisions sky rocketed to about 6 times what it was for the linked list methods. Unused space went down but clearly collisions are still an issue. Also time went up by a decent amount.

| Unused Space(Title Table) | 4999 |
| :---- | :---- |
| Unused Space(Quote Table) | 5000 |
| Collisions  (Title Table) | 65503 |
| Collisions  (Quote Table) | 73977 |
| Time to complete: | 0.11579 |

4. For attempt 4 I decided to try out a new hashing method but to keep using the linear probing method. For the new hashing method I took the value of the char string, multiplied it by 0.29 to reduce at a varying rate based on the value of the string, and then multiplied it by 10000 to move the decimal point producing a new number. I then floored the number so that I wouldn’t get invalid indexes. I had 20000 for the table size and I also improved the linear probing method by using a relatively large prime number(101).  
   1. Unused space stayed the same which is expected and collisions went way up. So this method clearly did not work well. The time did take almost twice as long as before but still only about a fifth of a second. In my opinion potentially the worst one yet.

| Unused Space(Title Table) | 5000 |
| :---- | :---- |
| Unused Space(Quote Table) | 5000 |
| Collisions  (Title Table) | 587803 |
| Collisions  (Quote Table) | 581702 |
| Time to complete: | 0.21775 |

      

5. For attempt 5 I decided to try to improve both by combining them(sort of). I used a double hash method for the table. This involved creating a smaller hash table within each index of the main hash table. I used the hash function that was my second attempt as that was my favorite. For the second smaller hash table I used the whichever(quote or title) that I didn’t use for my first hash table as the key.  
   1. By far the lowest collision rate of any of the methods, only 200 for the title and 0 for the quote. Unused space was relatively low although I question if I am calculating it correctly, I check every value in the interior hash table if a space \= None then it is counted as an empty space/wasted space. 

| Unused Space(Title Table) | 14898 |
| :---- | :---- |
| Unused Space(Quote Table) | 14898 |
| Collisions  (Title Table) | 200 |
| Collisions  (Quote Table) | 0 |
| Time to complete: | 0.255882 |

| Best time efficiency | Attempt 1 |
| :---- | :---- |
| Best space efficiency  | Attempt 3 |
| Least Collisions | Attempt 5 |

Overall I would say the best method is probably Attempt 2\. It had a decently low amount of unused space, the collisions were moderately low, and the time was the second quickest. While it wasn’t number 1 in any category I believe its overall performance was the best. I believe the reason for this was the hash function itself, it allowed for the best spread of my hash functions. It also was the linked list method which helped keep the collisions to a moderate amount. It was simple but effective which helped keep the time down. 
