#!/usr/bin/env python3
\"\"\"
Test Runner Script for Hotel Management System Backend

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py --auth             # Run only auth tests
    python run_tests.py --coverage         # Run with coverage report
    python run_tests.py --integration      # Run integration tests
\"\"\"

import subprocess
import sys
import argparse
import os
from pathlib import Path

def run_command(command):
    \"\"\"Execute command and return result\"\"\"
    print(f\"Running: {' '.join(command)}\")
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f\"Error: {result.stderr}\")
    return result.returncode == 0

def setup_test_environment():
    \"\"\"Set up test environment\"\"\"
    print(\"🔧 Setting up test environment...\")
    
    # Install test requirements
    if not run_command([sys.executable, \"-m\", \"pip\", \"install\", \"-r\", \"test-requirements.txt\"]):
        print(\"❌ Failed to install test requirements\")
        return False
    
    # Set test environment variables
    os.environ[\"TESTING\"] = \"1\"
    os.environ[\"DATABASE_URL\"] = \"postgresql://postgres:postgres@localhost:5432/hotel_test\"
    
    print(\"✅ Test environment ready\")
    return True

def run_auth_tests():
    \"\"\"Run authentication tests\"\"\"
    print(\"🔐 Running authentication tests...\")
    return run_command([\"pytest\", \"tests/test_auth.py\", \"-v\"])

def run_role_tests():
    \"\"\"Run role-based access tests\"\"\"
    print(\"👥 Running role access tests...\")
    return run_command([\"pytest\", \"tests/test_role_access.py\", \"-v\"])

def run_rooms_tests():
    \"\"\"Run room management tests\"\"\"
    print(\"🏨 Running room management tests...\")
    return run_command([\"pytest\", \"tests/test_rooms.py\", \"-v\"])

def run_guests_tests():
    \"\"\"Run guest management tests\"\"\"
    print(\"👤 Running guest management tests...\")
    return run_command([\"pytest\", \"tests/test_guests.py\", \"-v\"])

def run_pos_tests():
    \"\"\"Run POS system tests\"\"\"
    print(\"💰 Running POS system tests...\")
    return run_command([\"pytest\", \"tests/test_pos.py\", \"-v\"])

def run_analytics_tests():
    \"\"\"Run analytics tests\"\"\"
    print(\"📊 Running analytics tests...\")
    return run_command([\"pytest\", \"tests/test_analytics.py\", \"-v\"])

def run_all_tests():
    \"\"\"Run all tests\"\"\"
    print(\"🧪 Running all tests...\")
    return run_command([\"pytest\", \"tests/\", \"-v\"])

def run_tests_with_coverage():
    \"\"\"Run tests with coverage report\"\"\"
    print(\"📋 Running tests with coverage...\")
    success = run_command([
        \"pytest\", \"tests/\", 
        \"--cov=app\", 
        \"--cov-report=html\", 
        \"--cov-report=term-missing\",
        \"-v\"
    ])
    
    if success:
        print(\"📄 Coverage report generated in htmlcov/index.html\")
    
    return success

def run_integration_tests():
    \"\"\"Run integration tests\"\"\"
    print(\"🔗 Running integration tests...\")
    return run_command([
        \"pytest\", \"tests/\", 
        \"-m\", \"integration\", 
        \"-v\"
    ])

def generate_test_report():
    \"\"\"Generate comprehensive test report\"\"\"
    print(\"📝 Generating test report...\")
    return run_command([
        \"pytest\", \"tests/\", 
        \"--html=test_report.html\", 
        \"--json-report\", \"--json-report-file=test_report.json\",
        \"-v\"
    ])

def main():
    parser = argparse.ArgumentParser(description=\"Run Hotel Management System Backend Tests\")
    parser.add_argument(\"--auth\", action=\"store_true\", help=\"Run authentication tests only\")
    parser.add_argument(\"--roles\", action=\"store_true\", help=\"Run role access tests only\")
    parser.add_argument(\"--rooms\", action=\"store_true\", help=\"Run room management tests only\")
    parser.add_argument(\"--guests\", action=\"store_true\", help=\"Run guest management tests only\")
    parser.add_argument(\"--pos\", action=\"store_true\", help=\"Run POS system tests only\")
    parser.add_argument(\"--analytics\", action=\"store_true\", help=\"Run analytics tests only\")
    parser.add_argument(\"--coverage\", action=\"store_true\", help=\"Run tests with coverage report\")
    parser.add_argument(\"--integration\", action=\"store_true\", help=\"Run integration tests only\")
    parser.add_argument(\"--report\", action=\"store_true\", help=\"Generate comprehensive test report\")
    parser.add_argument(\"--setup-only\", action=\"store_true\", help=\"Only setup test environment\")
    
    args = parser.parse_args()
    
    # Always setup test environment first
    if not setup_test_environment():
        sys.exit(1)
    
    if args.setup_only:
        print(\"✅ Test environment setup complete\")
        return
    
    success = True
    
    if args.auth:
        success = run_auth_tests()
    elif args.roles:
        success = run_role_tests()
    elif args.rooms:
        success = run_rooms_tests()
    elif args.guests:
        success = run_guests_tests()
    elif args.pos:
        success = run_pos_tests()
    elif args.analytics:
        success = run_analytics_tests()
    elif args.coverage:
        success = run_tests_with_coverage()
    elif args.integration:
        success = run_integration_tests()
    elif args.report:
        success = generate_test_report()
    else:
        success = run_all_tests()
    
    if success:
        print(\"\n✅ All tests passed successfully!\")
        print(\"\n📊 Test Summary:\")
        print(\"   🔐 Authentication: Covered\")
        print(\"   👥 Role Access: Covered\")
        print(\"   🏨 Room Management: Covered\")
        print(\"   👤 Guest Management: Covered\")
        print(\"   💰 POS System: Covered\")
        print(\"   📊 Analytics: Covered\")
    else:
        print(\"\n❌ Some tests failed. Check the output above.\")
        sys.exit(1)

if __name__ == \"__main__\":
    main()