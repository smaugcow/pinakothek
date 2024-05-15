import unittest
from structure_diagram import dot  # assuming structure_diagram and test_structure_diagram are in the same directory

class TestStructureDiagram(unittest.TestCase):
    def test_nodes_exist(self):
        """ Test if all nodes are created. """
        expected_nodes = {'User', 'Frontend', 'Content', 'Backend', 'DB', 'Admin', 'Pinakothek',
                          'Authorization', 'ContentManagement', 'ContentDisplay', 'MediaProcessing', 'DataStorage',
                          'Fields1', 'Methods1', 'Fields2', 'Methods2', 'Fields3', 'Fields4', 'Fields5'}
        actual_nodes = set([node.get_name() for node in dot.get_nodes()])
        self.assertTrue(expected_nodes.issubset(actual_nodes))
    def test_edges_exist(self):
        """ Test if all edges are correctly created. """
        expected_edges = [
            ('Pinakothek', 'Authorization'), ('Pinakothek', 'ContentManagement'),
            ('Pinakothek', 'ContentDisplay'), ('Pinakothek', 'MediaProcessing'), ('Pinakothek', 'DataStorage'),
            ('Authorization', 'Fields1'), ('Authorization', 'Methods1'),
            ('ContentManagement', 'Fields2'), ('ContentManagement', 'Methods2'),
            ('ContentDisplay', 'Fields3'), ('MediaProcessing', 'Fields4'), ('DataStorage', 'Fields5'),
            ('User', 'Authorization'), ('Frontend', 'ContentDisplay'), ('Content', 'ContentManagement'),
            ('Backend', 'MediaProcessing'), ('DB', 'DataStorage'), ('Admin', 'Authorization')
        ]
        actual_edges = [(edge.get_source(), edge.get_destination()) for edge in dot.get_edges()]
        for edge in expected_edges:
            self.assertIn(edge, actual_edges)
if name == 'main':
    unittest.main()
   
