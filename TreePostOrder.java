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

public class TreePostOrder 
{
    Node root;

    public TreePostOrder() {}

    public TreePostOrder(Node node){
        root = node;
    }
     
    void bottomView() 
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
        Node root = new Node(5);
        root.left = new Node(3);
        root.left.left = new Node(1);
        root.left.left.left = new Node(0);
        root.left.right = new Node(4);
        root.right = new Node(7);
        root.right.left = new Node(6);
        root.right.right = new Node(9);
        root.right.right.left = new Node(8);
        TreePostOrder tree = new TreePostOrder(root);
        
        System.out.println("The Bottom View of Binary Tree by Postorder is: ");
        tree.bottomView(); 
        System.out.println();
    } 
     
}