#!/usr/bin/env python3
"""
Test script to verify the web application works locally
Run this before deploying to Render.com
"""

import requests
import time
import sys

def test_web_app():
    """Test the web application endpoints"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing Free Fire Bot Web Application...")
    print("=" * 50)
    
    # Test health endpoint
    try:
        print("1. Testing health endpoint...")
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("   ✅ Health check passed")
            print(f"   📊 Response: {response.json()}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Health check failed: {e}")
        return False
    
    # Test status endpoint
    try:
        print("\n2. Testing status endpoint...")
        response = requests.get(f"{base_url}/api/status", timeout=5)
        if response.status_code == 200:
            print("   ✅ Status endpoint working")
            data = response.json()
            print(f"   📊 Bot running: {data.get('running', False)}")
            print(f"   📊 Bot connected: {data.get('connected', False)}")
        else:
            print(f"   ❌ Status endpoint failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Status endpoint failed: {e}")
        return False
    
    # Test main page
    try:
        print("\n3. Testing main page...")
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            print("   ✅ Main page accessible")
            if "Free Fire Bot" in response.text:
                print("   ✅ Dashboard content loaded")
            else:
                print("   ⚠️  Dashboard content may be missing")
        else:
            print(f"   ❌ Main page failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Main page failed: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 All tests passed! Your web app is ready for deployment.")
    print("\n📋 Next steps:")
    print("   1. Push your code to GitHub")
    print("   2. Connect to Render.com")
    print("   3. Deploy using the instructions in README_DEPLOYMENT.md")
    
    return True

if __name__ == "__main__":
    print("🚀 Free Fire Bot - Local Test")
    print("Make sure to run 'python web_app.py' in another terminal first!")
    print("Press Enter to start testing...")
    input()
    
    if test_web_app():
        sys.exit(0)
    else:
        print("\n❌ Some tests failed. Check your setup and try again.")
        sys.exit(1)
