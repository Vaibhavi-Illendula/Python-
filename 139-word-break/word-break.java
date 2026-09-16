// class Solution {
//     public boolean wordBreak(String s, List<String> wordDict) {

//         boolean[] dp = new boolean[s.length() + 1];

//         dp[0] = true;

//         for (int i = 1; i <= s.length(); i++) {

//             for (String word : wordDict) {

//                 int len = word.length();

//                 if (i >= len) {

//                     if (dp[i - len] && s.substring(i - len, i).equals(word)) {
//                         dp[i] = true;
//                         break;
//                     }
//                 }
//             }
//         }

//         return dp[s.length()];
//     }
// }


import java.util.*;
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
     Set<String> set = new HashSet<>(wordDict);
     boolean[] d = new boolean[s.length()+1];
     d[0]=true;
     for(int i=1;i<=s.length();i++)
     {
        for(int j=0;j<i;j++)
        {
            if(d[j] && set.contains(s.substring(j,i)))
            {
                d[i]=true;
                break;
            }
        }
     }

     return d[s.length()];
    }
}