/* Node structure  used in the program

struct Node{
	int data;
	struct Node * next;
	struct Node * bottom;
	
	Node(int x){
	    data = x;
	    next = NULL;
	    bottom = NULL;
	}
	
};
*/
Node *merge2List(Node *l1, Node *l2){
    Node *temp = new Node(0);
    Node *res = temp;
    
    while(l1!=NULL and l2!=NULL){
        if(l1->data < l2->data){
            temp->bottom = l1;
            l1 = l1->bottom;
        }
        else{
            temp->bottom = l2;
            l2 = l2->bottom;
        }
        temp = temp->bottom;
    }
    
    if(l1!=NULL) temp->bottom = l1;
    else temp->bottom = l2;
    
    return res->bottom;
}

/*  Function which returns the  root of 
    the flattened linked list. */
Node *flatten(Node *root)
{
   // Your code here
   if(root==NULL || root->next==NULL){
       return root;
   }
   
   root->next = flatten(root->next);
   return merge2List(root, root->next);
}