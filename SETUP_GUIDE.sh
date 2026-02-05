#!/bin/bash
# ============================================
# LeetCode Python Repo Setup Script
# Run this in your terminal step by step
# ============================================

# ---- STEP 1: Create the repo on GitHub FIRST ----
# Go to https://github.com/new
# Name: daily-coding-challenges
# Description: Daily coding challenges in Python — LeetCode, algorithms, and more
# Make it PUBLIC
# Do NOT check "Add a README file"
# Click "Create repository"

# ---- STEP 2: Navigate to where you want the repo ----
# cd ~/Desktop   (or wherever you keep your projects)

# ---- STEP 3: Clone or init ----
# Option A — If you created the repo on GitHub first:
# git clone https://github.com/mazlumunay/daily-coding-challenges.git
# cd leetcode-python

# Option B — If you want to init locally first:
# mkdir leetcode-python
# cd leetcode-python
# git init

# ---- STEP 4: Copy all the files from this download into the repo folder ----
# Copy: README.md, ROADMAP.md, TEMPLATE.py, .gitignore
# Copy: easy/ folder (with the 2 starter problems)
# Copy: medium/ folder (empty for now)
# Copy: hard/ folder (empty for now)

# ---- STEP 5: Add placeholder files so empty folders get tracked ----
# touch medium/.gitkeep
# touch hard/.gitkeep

# ---- STEP 6: First commit ----
# git add .
# git commit -m "Initial setup: LeetCode daily challenge repo with roadmap and first 2 solutions"

# ---- STEP 7: Connect to GitHub (skip if you cloned) ----
# git remote add origin https://github.com/mazlumunay/daily-coding-challenges.git
# git branch -M main
# git push -u origin main

# ---- STEP 8: Verify ----
# Go to https://github.com/mazlumunay/daily-coding-challenges
# You should see your README rendered beautifully!

# ============================================
# DAILY WORKFLOW (do this every day)
# ============================================

# 1. Copy TEMPLATE.py to the right folder:
#    cp TEMPLATE.py easy/XXX_problem_name.py

# 2. Solve the problem in that file

# 3. Add, commit, push:
#    git add .
#    git commit -m "Add #XXX Problem Name - O(n) approach"
#    git push

# That's it! Your GitHub stays green. 💚
