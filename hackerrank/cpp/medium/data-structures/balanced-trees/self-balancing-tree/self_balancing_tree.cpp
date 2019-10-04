// recursively return the height of the given node
int get_height(node* root) {
    if (!root)  return -1;
    return max(1+get_height(root->left), 1+get_height(root->right));
}
//
void update(node* root)
{
    if (root)   root->ht = 1+max(get_height(root->left), get_height(root->right));
}
void rotate_with_left_child(node*& root)
{
    node* tmp = root->left;
    root->left = tmp->right;
    tmp->right = root;
    root=tmp;
    update(root->right);
    update(root);
}
void rotate_with_right_child(node*& root)
{
    node* tmp = root->right;
    root->right = tmp->left;
    tmp->left = root;
    root=tmp;
    update(root->left);
    update(root);
}

void balance(node*& root) {
    if (get_height(root->left)-get_height(root->right) > 1)
        if (get_height(root->left->left)>=get_height(root->left->right)) rotate_with_left_child(root);
        else
        {
            rotate_with_right_child(root->left);
            rotate_with_left_child(root);
        }
    else if (get_height(root->right)-get_height(root->left)>1)
        if(get_height(root->right->right)>=get_height(root->right->left))  rotate_with_right_child(root);
        else
        {
            rotate_with_left_child(root->right);
            rotate_with_right_child(root);
        }
}

node * insert(node*& root,int& val)
{
     if (!root) {   root = new node; root->val = val;}
     else if (val<root->val)    insert(root->left, val);
     else if (val>root->val)    insert(root->right, val);

     balance(root);
     root->ht = get_height(root);
     return root;
}
