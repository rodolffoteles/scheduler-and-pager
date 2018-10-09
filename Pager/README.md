# Pager
In a operating systems that use paging for memory management, page replacement algorithm are needed to decide which page needs to be replaced when new page comes in. Whenever a new page is referred and not present in memory, page fault occurs and the operating system replaces one of the existing pages with newly needed page. Here you have to calculate the number of page faults with three different algorithms (first in first out, optimal page replacement, least recently used). 

## Input
The first line of input contains one integer indicating the number of frame slots. The next lines consists of several integers numbers, one per line, corresponding to the number of the page referenced by the process.

## Output
For each algorithm print a new line with the algorithm's initials followed by the number of page faults that occured.

| Input Sample                                                | Output Sample            |
|-------------------------------------------------------------|--------------------------|
|4<br>1<br>2<br>3<br>4<br>1<br>2<br>5<br>1<br>2<br>3<br>4<br>5| FIFO 10<br>OTM 6<br>LRU 8|


