"""
Quick start script - Run the platform after setup
"""
import subprocess
import sys
import os
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and print output"""
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return process
    except Exception as e:
        print(f"Error running command: {e}")
        return None

def main():
    print("=" * 50)
    print("🚀 Starting AI E-commerce Platform")
    print("=" * 50)
    print()
    
    # Check if we're in the right directory
    backend_path = Path("backend")
    if not backend_path.exists():
        print("❌ Error: backend directory not found")
        print("Please run this script from the project root directory")
        sys.exit(1)
    
    print("📦 Starting Django backend server...")
    print("   Backend will be available at: http://localhost:8000")
    print("   Django Admin at: http://localhost:8000/admin")
    print()
    
    # Start Django server
    django_process = run_command(
        "python manage.py runserver",
        cwd=str(backend_path)
    )
    
    if django_process:
        print("✅ Backend server started!")
        print()
        print("=" * 50)
        print("ℹ️  Platform is running!")
        print("=" * 50)
        print()
        print("📍 Access points:")
        print("   - Backend API: http://localhost:8000")
        print("   - Django Admin: http://localhost:8000/admin")
        print("   - API Docs: http://localhost:8000/api/")
        print()
        print("🎨 To start the admin dashboard:")
        print("   1. Open a new terminal")
        print("   2. cd frontend/admin")
        print("   3. npm install (first time only)")
        print("   4. npm run dev")
        print("   5. Visit http://localhost:5173")
        print()
        print("Press Ctrl+C to stop the server")
        print()
        
        try:
            django_process.wait()
        except KeyboardInterrupt:
            print("\n\n🛑 Shutting down...")
            django_process.terminate()
            print("✅ Server stopped")
    else:
        print("❌ Failed to start backend server")
        sys.exit(1)

if __name__ == "__main__":
    main()
