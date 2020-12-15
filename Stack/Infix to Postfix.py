"""// { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while(t-->0){
            System.out.println(new solve().infixToPostfix(br.readLine().trim()));
        }
    }
}// } Driver Code Ends

class solve{
    public static String infixToPostfix(String exp) {
        Deque<String> stack = new ArrayDeque<>();
        String out = "", ops = "-+/*^()";
        for (int i = 0; i < exp.length(); ++i) {
            String s = String.valueOf(exp.charAt(i));
            String p = stack.isEmpty() ? "" : stack.peek();
            int a = prec(s), b = prec(p);
            if (!ops.contains(s)) out += s;
            else if (s.equals("(") || a > b) stack.push(s);
            else if (s.equals(")")) {
                while (!stack.peek().equals("(")) out += stack.pop();
                stack.pop();
            }
            else {
                while (!p.equals("(") && a <= b) {
                    out += stack.pop();
                    p = stack.isEmpty() ? "" : stack.peek();
                    b = prec(p);
                }
                stack.push(s);
            }
        }
        while(!stack.isEmpty()) out += stack.pop();
        return out;
    }

    public static int prec(String s) {
        int i;
        switch(s) {
            case "^": i = 4; break;
            case "*":
            case "/": i = 3; break;
            case "+":
            case "-": i = 1; break;
            default: i = 0;
        }
        return i;
    }
}
"""