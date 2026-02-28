# test_backnebula.py
"""
Tests for BackNebula module.
"""

import unittest
from backnebula import BackNebula

class TestBackNebula(unittest.TestCase):
    """Test cases for BackNebula class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BackNebula()
        self.assertIsInstance(instance, BackNebula)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BackNebula()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
