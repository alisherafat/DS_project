from src.tree import ExpressionTree

exp_tree = ExpressionTree("((5+4)*2)+8")
print("Infix: ", end='')
exp_tree.inorder(exp_tree.root)
print("\nPostfix: ", end='')
exp_tree.post_order(exp_tree.root)
print("\nPrefix: ", end='')
exp_tree.pre_order(exp_tree.root)
print()
print(exp_tree.evaluate(exp_tree.root))

