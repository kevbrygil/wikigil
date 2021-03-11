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

public class BottomViewTreeInOrder {
    Node root;

    void bottomView(Node root) {
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

        BottomViewTreeInOrder tree = new BottomViewTreeInOrder();
        tree.root = new Node(5);
        tree.root.left = new Node(3);
        tree.root.left.left = new Node(1);
        tree.root.left.left.left = new Node(0);
        tree.root.left.right = new Node(4);
        tree.root.right = new Node(7);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(9);
        tree.root.right.right.left = new Node(8);

        System.out.println("The Bottom View of Binary Tree by Inorder is: ");
        tree.bottomView(tree.root); 
        System.out.println();
    }

}