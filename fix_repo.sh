#!/bin/bash

echo "🔧 Fixing repository..."

# Create .gitignore
cat > .gitignore << 'EOL'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv

# Flask
instance/
.webassets-cache

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment
.env
.flaskenv

# Database
*.db
*.sqlite
*.sqlite3

# Logs
*.log
EOL

echo "✅ Created .gitignore"

# Remove all cached files
git rm -r --cached . 2>/dev/null

# Add everything back (respecting .gitignore)
git add .

# Commit
git commit -m "Add .gitignore and clean up repository"

# Push
git push origin main

echo "✅ Repository cleaned!"
echo "🎉 Done! Check your GitHub repository now."