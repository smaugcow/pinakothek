from graphviz import Digraph

# Initialize Graphviz object
dot = Digraph()

# Define entities
dot.node('User', 'User')
dot.node('Frontend', 'Frontend')
dot.node('Content', 'Content')
dot.node('Backend', 'Backend')
dot.node('DB', 'Database (SQLite)')
dot.node('Admin', 'Admin')

# Define abstraction blocks
dot.node('Pinakothek', 'Pinakothek\nWeb Application')
dot.node('Authorization', 'Authorization\n& Authentication')
dot.node('ContentManagement', 'Content Management')
dot.node('ContentDisplay', 'Content Display')
dot.node('MediaProcessing', 'Media Processing')
dot.node('DataStorage', 'Data Storage')

# Define fields and methods within the abstraction blocks
dot.node('Fields1', 'Fields: \n- User Data\n- Login Sessions', shape='box')
dot.node('Methods1', 'Methods: \n- Register User\n- Log In\n- Log Out', shape='box')
dot.node('Fields2', 'Fields: \n- Upload/Delete/Edit\n- Media Description', shape='box')
dot.node('Methods2', 'Methods: \n- Upload Media\n- Delete Media\n- Edit Media', shape='box')
dot.node('Fields3', 'Fields: \n- Gallery View\n- Pagination\n- Filtering', shape='box')
dot.node('Fields4', 'Fields: \n- Pillow (Images)\n- FFmpeg (Videos)', shape='box')
dot.node('Fields5', 'Fields: \n- SQLite\n- Stored Files Info', shape='box')

# add dependency connections between abstraction blocks and entities
dot.edge('Pinakothek', 'Authorization')
dot.edge('Pinakothek', 'ContentManagement')
dot.edge('Pinakothek', 'ContentDisplay')
dot.edge('Pinakothek', 'MediaProcessing')
dot.edge('Pinakothek', 'DataStorage')

dot.edge('Authorization', 'Fields1')
dot.edge('Authorization', 'Methods1')
dot.edge('ContentManagement', 'Fields2')
dot.edge('ContentManagement', 'Methods2')
dot.edge('ContentDisplay', 'Fields3')
dot.edge('MediaProcessing', 'Fields4')
dot.edge('DataStorage', 'Fields5')

# add connections between entities and abstraction blocks
dot.edge('User', 'Authorization')
dot.edge('Frontend', 'ContentDisplay')
dot.edge('Content', 'ContentManagement')
dot.edge('Backend', 'MediaProcessing')
dot.edge('DB', 'DataStorage')
dot.edge('Admin', 'Authorization')

# save and render the diagram
dot.render('pinakothek_structure_updated', format='png', view=True)

print("Goob bay")
