import java.util.TreeMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Stack; 

class Node {
    int data;
    Node left, right;
 
    public Node(int data) {
        this.data = data;
        left = right = null;
    }
}

class NodeHD{
    Node node;
    int hd;

    NodeHD(Node node, int hd) {
        this.node = node;
        this.hd = hd;
    }
}

public class BottomViewTreePostOrder 
{
    Node root;
     
    void bottomView(Node root) 
    {
        if (root == null)
            return;   
        
        Stack<NodeHD> nodeHDStack = new Stack<NodeHD>();
        
        Map<Integer,Integer> bottomView = new TreeMap<>();
 
        nodeHDStack.add(new NodeHD(root, 0));

        Node previous = null; 

        while (!nodeHDStack.isEmpty()) 
        {
            NodeHD current = nodeHDStack.peek();
            int hd=current.hd;
            Node tempNode=current.node;

            if(previous == null || previous.left == tempNode || previous.right == tempNode){
                if(tempNode.left != null)
                    nodeHDStack.push(new NodeHD(tempNode.left, hd - 1));
                else if (tempNode.right != null) 
                    nodeHDStack.push(new NodeHD(tempNode.right, hd + 1)); 
                else{ 
                    nodeHDStack.pop(); 
                    bottomView.put(hd,tempNode.data); 
                } 
            }
            else if (tempNode.left == previous) { 
                if (tempNode.right != null) 
                    nodeHDStack.push(new NodeHD(tempNode.right, hd + 1)); 
                else{ 
                    nodeHDStack.pop(); 
                    bottomView.put(hd,tempNode.data); 
                } 
            } 
            else if (tempNode.right == previous) { 
                nodeHDStack.pop(); 
                bottomView.put(hd,tempNode.data); 
            } 

            previous = tempNode;
 
        }
        for (Entry<Integer, Integer> entry : bottomView.entrySet()) 
        {
            System.out.print(entry.getValue()+" ");
        }
    }
    public static void main(String[] args) 
    { 
        BottomViewTreePostOrder tree = new BottomViewTreePostOrder();
        tree.root = new Node(5);
        tree.root.left = new Node(3);
        tree.root.left.left = new Node(1);
        tree.root.left.left.left = new Node(0);
        tree.root.left.right = new Node(4);
        tree.root.right = new Node(7);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(9);
        tree.root.right.right.left = new Node(8);
        
        System.out.println("The Bottom View of Binary Tree by Postorder is: ");
        tree.bottomView(tree.root); 
        System.out.println();
    } 
     
}