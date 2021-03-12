import java.util.Queue;
import java.util.TreeMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Map.Entry;

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

public class TreeInOrder {
    Node root;

    public TreeInOrder() {}

    public TreeInOrder(Node node){
        root = node;
    }

    void bottomView() {
        if (root == null)
            return;

        Queue<NodeHD> nodeHDQueue = new LinkedList<NodeHD>();

        Map<Integer, Integer> bottomView = new TreeMap<>();

        nodeHDQueue.add(new NodeHD(root, 0));

        while (!nodeHDQueue.isEmpty()) {
            NodeHD nodeHDCurrent = nodeHDQueue.poll();
            Node tempNode = nodeHDCurrent.node;
            int hd = nodeHDCurrent.hd;
            
            bottomView.put(hd, tempNode.data);

            if (tempNode.left != null) 
                nodeHDQueue.add(new NodeHD(tempNode.left, hd - 1));

            if (tempNode.right != null) 
                nodeHDQueue.add(new NodeHD(tempNode.right, hd + 1));

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
        TreeInOrder tree = new TreeInOrder(root);

        System.out.println("The Bottom View of Binary Tree by Inorder is: ");
        tree.bottomView(); 
        System.out.println();
    }

}