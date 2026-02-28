#!/usr/bin/env python3
"""
Test runner for skill_manager tests.
Provides convenient command-line interface for running tests.
"""

import sys
import unittest
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from test_skill_manager import (
    TestSkillVersionManager,
    TestSkillRegistry,
    TestSkillDependencyResolver,
    TestSkillCompatibilityChecker
)


def run_tests(verbosity=2):
    """Run all tests with specified verbosity."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestSkillVersionManager))
    suite.addTests(loader.loadTestsFromTestCase(TestSkillRegistry))
    suite.addTests(loader.loadTestsFromTestCase(TestSkillDependencyResolver))
    suite.addTests(loader.loadTestsFromTestCase(TestSkillCompatibilityChecker))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run skill manager tests')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Increase output verbosity')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Decrease output verbosity')
    
    args = parser.parse_args()
    
    verbosity = 2
    if args.verbose:
        verbosity = 3
    elif args.quiet:
        verbosity = 1
    
    return run_tests(verbosity)


if __name__ == '__main__':
    sys.exit(main())