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

public class TreePreOrder {
    Node root;

    public TreePreOrder() {}

    public TreePreOrder(Node node){
        root = node;
    }

    void bottomView() {
        if (root == null)
            return;

        Stack<NodeHD> nodeHDStack = new Stack<NodeHD>();

        Map<Integer, Integer> bottomView = new TreeMap<>();

        nodeHDStack.add(new NodeHD(root, 0));

        while (!nodeHDStack.isEmpty()) {
            NodeHD current = nodeHDStack.peek();
            int hd=current.hd;
            Node tempNode=current.node;
            nodeHDStack.pop();
            bottomView.put(hd, tempNode.data);

            if (tempNode.right != null) 
                nodeHDStack.push(new NodeHD(tempNode.right, hd + 1)); 

            if (tempNode.left != null) 
                nodeHDStack.push(new NodeHD(tempNode.left, hd - 1));

        }

        for (Entry<Integer, Integer> entry : bottomView.entrySet()) {
            System.out.print(entry.getValue() + " ");
        }
    }

    public static void main(String[] args) {

        Node root = new Node(5);
        root.left = new Node(3);
        root.left.left = new Node(1);
        root.left.left.left = new Node(0);
        root.left.right = new Node(4);
        root.right = new Node(7);
        root.right.left = new Node(6);
        root.right.right = new Node(9);
        root.right.right.left = new Node(8);
        TreePreOrder tree = new TreePreOrder(root);

        System.out.println("The Bottom View of Binary Tree by Preorder is: ");
        tree.bottomView(); 
        System.out.println();
    }

}