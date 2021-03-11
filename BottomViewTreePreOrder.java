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

public class BottomViewTreePreOrder {
    Node root;

    void bottomView(Node root) {
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

        BottomViewTreePreOrder tree = new BottomViewTreePreOrder();
        tree.root = new Node(5);
        tree.root.left = new Node(3);
        tree.root.left.left = new Node(1);
        tree.root.left.left.left = new Node(0);
        tree.root.left.right = new Node(4);
        tree.root.right = new Node(7);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(9);
        tree.root.right.right.left = new Node(8);

        System.out.println("The Bottom View of Binary Tree by Preorder is: ");
        tree.bottomView(tree.root); 
        System.out.println();
    }

}